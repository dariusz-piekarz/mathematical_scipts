"""Local API for the mathematical library (FastAPI).

Run from the repository root:
    python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765

Canonical sources and the SQLite index remain read-only. Generated drafts and explicitly saved copies are written to separate workspace directories.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from contextlib import asynccontextmanager
import asyncio
from contextlib import contextmanager
from pathlib import Path
from typing import Annotated, Any, Literal
import os
import sqlite3

import networkx as nx
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from backend.latex_parser import analyze_selection, get_stats, show_label
from backend import workspaces
from backend.concept_graph import build_concept_graph
from backend import lean_catalog
from backend import lean_formalization

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Recover orphaned drafts after crashes and prune them periodically."""
    workspaces.cleanup_stale_drafts()
    async def sweep():
        while True:
            await asyncio.sleep(15 * 60)
            workspaces.cleanup_stale_drafts()
    task = asyncio.create_task(sweep())
    try:
        yield
    finally:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        workspaces.cleanup_stale_drafts(ttl_seconds=0)


app = FastAPI(title="Biblioteka matematyczna — API", version="0.4.0", docs_url="/api/docs", redoc_url=None, lifespan=lifespan)
app.mount("/assets", StaticFiles(directory=FRONTEND), name="assets")


def database_path() -> Path:
    return Path(os.environ.get("MATLIB_DB", str(ROOT / "data" / "biblioteka.db"))).expanduser().resolve()


@contextmanager
def db_connection():
    path = database_path()
    if not path.is_file():
        raise HTTPException(status_code=503, detail=f"Nie znaleziono indeksu SQLite: {path.name}; uruchom index.")
    # Explicit read-only mode: API never changes documents, labels or modules.
    con = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=5)
    con.row_factory = sqlite3.Row
    try:
        yield con
    finally:
        con.close()


def sql_like(value: str) -> str:
    return "%" + value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"


def require_document(con: sqlite3.Connection, module_id: str) -> sqlite3.Row:
    row = con.execute("SELECT id,title,domain,path,sha256,length(content) AS length FROM documents WHERE id=?", (module_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Nieznany moduł.")
    return row


def entity_row(con: sqlite3.Connection, entity_id: str) -> sqlite3.Row:
    row = con.execute("SELECT e.*, d.title AS document_title,d.domain AS domain FROM entities e JOIN documents d ON e.document_id=d.id WHERE e.id=?", (entity_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Nieznany obiekt matematyczny.")
    return row


def entity_payload(row: sqlite3.Row) -> dict[str, Any]:
    return {key:row[key] for key in ("id", "document_id", "parent_id", "kind", "subtype", "title", "start_offset", "end_offset", "start_line", "end_line", "excerpt", "starred")}


@app.get("/")
def index():
    return FileResponse(FRONTEND / "index.html")


@app.get("/api/health")
def health():
    path = database_path()
    return {"ok":path.exists(), "db":"biblioteka.db", "readonly":True, "version":"0.4.0"}


@app.get("/api/stats")
def stats():
    with db_connection() as con:
        return get_stats(con)


@app.get("/api/domains")
def domains():
    with db_connection() as con:
        return [{"name":r["domain"], "modules":r["modules"],"entities":r["entities"]}
                for r in con.execute("""SELECT d.domain,count(DISTINCT d.id) AS modules,count(e.id) AS entities
                 FROM documents d LEFT JOIN entities e ON e.document_id=d.id
                 GROUP BY d.domain ORDER BY d.domain""")]


@app.get("/api/modules")
def modules(domain: str | None = None, q: str = "", limit: Annotated[int,Query(ge=1,le=500)] = 300,
            offset: Annotated[int,Query(ge=0)] = 0):
    where = ["1=1"]
    params: list[Any] = []
    if domain:
        where.append("domain=?"); params.append(domain)
    if q.strip():
        where.append("(title LIKE ? ESCAPE '\\' OR id LIKE ? ESCAPE '\\')")
        params += [sql_like(q.strip())]*2
    with db_connection() as con:
        sql_where = " AND ".join(where)
        count = con.execute(f"SELECT count(*) FROM documents WHERE {sql_where}",params).fetchone()[0]
        rows = con.execute(f"SELECT id,title,domain,path,length(content) AS length FROM documents WHERE {sql_where} ORDER BY domain,id LIMIT ? OFFSET ?", (*params, limit, offset)).fetchall()
        return {"total":count,"items":[dict(x) for x in rows]}


@app.get("/api/modules/{module_id}/outline")
def outline(module_id: str, kind: str | None = None):
    with db_connection() as con:
        doc = require_document(con,module_id)
        rows = con.execute("SELECT id,document_id,parent_id,kind,subtype,title,start_offset,end_offset,start_line,end_line,excerpt,starred FROM entities WHERE document_id=? ORDER BY start_offset,end_offset DESC", (module_id,)).fetchall()
        label_index: dict[str,list[str]] = defaultdict(list)
        for r in con.execute("SELECT name,entity_id FROM labels WHERE document_id=?",(module_id,)):
            if r["entity_id"]: label_index[r["entity_id"]].append(r["name"])
        children = Counter(r["parent_id"] for r in rows if r["parent_id"])
        visible = [r for r in rows if not kind or r["kind"] == kind]
        return {"module":dict(doc), "total":len(rows),"entities":[{**entity_payload(r), "labels":label_index.get(r["id"],[]),"has_children":children[r["id"]] > 0} for r in visible]}


@app.get("/api/modules/{module_id}")
def module_detail(module_id: str, full: bool = False):
    with db_connection() as con:
        doc = require_document(con,module_id)
        row = con.execute("SELECT content FROM documents WHERE id=?",(module_id,)).fetchone()
        content = row["content"]
        limit = None if full else 32000
        return {"module":dict(doc),"latex":content[:limit] if limit else content,
                "truncated":bool(limit and len(content)>limit),"full_length":len(content)}


@app.get("/api/entities/{entity_id:path}")
def entity_detail(entity_id: str, full: bool = False):
    with db_connection() as con:
        row = entity_row(con,entity_id)
        doc = con.execute("SELECT content FROM documents WHERE id=?",(row["document_id"],)).fetchone()
        content = doc["content"][row["start_offset"]:row["end_offset"]]
        limit = None if full else 26000
        labels = [r[0] for r in con.execute("SELECT name FROM labels WHERE entity_id=? ORDER BY offset",(entity_id,))]
        return {"entity":entity_payload(row),"module_title":row["document_title"],"domain":row["domain"],
                "labels":labels,"latex":content[:limit] if limit else content,
                "truncated":bool(limit and len(content)>limit), "full_length":len(content)}



@app.get("/api/lean/status")
def lean_toolchain_status():
    """Local availability of the trusted, explicitly enabled Lean runner."""
    return lean_formalization.availability()


@app.get("/api/lean/catalog")
def lean_catalog_index():
    """Browse registered mappings, independently of compilation status."""
    with db_connection() as con:
        return lean_catalog.list_formalizations(con)


@app.get("/api/lean/fragment")
def lean_fragment(entity_id: str | None = None, module_id: str | None = None,
                  start_line: Annotated[int | None, Query(ge=1)] = None,
                  end_line: Annotated[int | None, Query(ge=1)] = None):
    """Show exact indexed LaTeX and registered Lean code; never synthesize proof status."""
    with db_connection() as con:
        return lean_formalization.fragment(
            con, entity_id=entity_id, module_id=module_id,
            start_line=start_line, end_line=end_line)


class LeanRunRequest(BaseModel):
    formalization_id: str = Field(min_length=1, max_length=100)


@app.post("/api/lean/run")
def lean_run(request: LeanRunRequest):
    """Run only a registered repository Lean file, never browser-provided code."""
    with db_connection() as con:
        return lean_formalization.run(con, request.formalization_id)


@app.get("/api/labels/{label:path}")
def label_detail(label: str, source_document: str | None = None):
    if len(label)>300:
        raise HTTPException(status_code=400,detail="Zbyt długa etykieta.")
    if source_document is not None and len(source_document)>100:
        raise HTTPException(status_code=400,detail="Zbyt długi identyfikator źródła.")
    with db_connection() as con:
        if source_document:
            resolved = con.execute("""SELECT DISTINCT target_document,target_entity,status
                FROM references_tex WHERE source_document=? AND target_label=?
                  AND target_document IS NOT NULL
                  AND status IN ('resolved','external_resolved','alias_resolved','included_resolved')""",
                  (source_document,label)).fetchall()
            targets = {(r["target_document"],r["target_entity"]) for r in resolved}
            if len(targets) == 1:
                target_document,target_entity = next(iter(targets))
                actual = con.execute("""SELECT name FROM label_occurrences
                    WHERE document_id=? AND (entity_id=? OR name=?)
                    ORDER BY CASE WHEN name=? THEN 0 ELSE 1 END, line LIMIT 1""",
                    (target_document,target_entity,label,label)).fetchone()
                if not actual and resolved[0]["status"] == "included_resolved":
                    provenance = con.execute("""SELECT origin_path,origin_line,origin_offset
                        FROM included_label_origins WHERE document_id=? AND name=?
                        ORDER BY origin_path,origin_line LIMIT 1""",
                        (target_document,label)).fetchone()
                    if provenance is not None:
                        root = ROOT.parent.resolve()
                        origin = (root / provenance["origin_path"]).resolve()
                        if origin.is_relative_to(root) and origin.is_file():
                            content = origin.read_text(encoding="utf-8-sig")
                            position = provenance["origin_offset"]
                            title = con.execute("SELECT title FROM documents WHERE id=?",
                                                (target_document,)).fetchone()["title"]
                            return {"name":label,"canonical_label":label,
                                    "document_id":target_document,"entity_id":None,
                                    "source_document":source_document,
                                    "occurrence_id":f"{target_document}::included::{label}",
                                    "resolution_status":"included_resolved",
                                    "origin_path":provenance["origin_path"],
                                    "origin_line":provenance["origin_line"],
                                    "title":title,"line":provenance["origin_line"],
                                    "latex":content[max(0,position-140):position+1560],
                                    "incoming_references":len(resolved)}
                if actual:
                    result = show_label(con,actual["name"],max_chars=1700,document_id=target_document)
                    if result is not None:
                        result["canonical_label"] = actual["name"]
                        result["name"] = label
                        result["source_document"] = source_document
                        result["occurrence_id"] = f"{target_document}::{actual['name']}"
                        result["resolution_status"] = resolved[0]["status"]
                        result["incoming_references"] = con.execute(
                            "SELECT count(*) FROM references_tex WHERE target_label=? AND source_document=?",
                            (label,source_document)).fetchone()[0]
                        return result
        options = con.execute("""SELECT c.document_id,c.line,c.entity_id,d.title,d.domain
             FROM label_conflicts c JOIN documents d ON d.id=c.document_id
             WHERE c.name=? ORDER BY c.document_id""", (label,)).fetchall()
        if options:
            count = con.execute("SELECT count(*) FROM references_tex WHERE target_label=?", (label,)).fetchone()[0]
            return {"name":label,"ambiguous":True,"candidates":[dict(x) for x in options],
                    "incoming_references":count}
        result = show_label(con,label,max_chars=1700)
        if not result:
            raise HTTPException(status_code=404,detail="Etykieta nie istnieje.")
        count = con.execute("SELECT count(*) FROM references_tex WHERE target_label=?",(label,)).fetchone()[0]
        result["incoming_references"] = count
        return result


@app.get("/api/search")
def search(q: Annotated[str,Query(min_length=1,max_length=150)],
           domain: str | None = None, kind: str | None = None,
           limit: Annotated[int,Query(ge=1,le=100)] = 30):
    with db_connection() as con:
        results: list[dict[str, Any]]=[]
        if kind != "module":
            where = ["(e.title LIKE ? ESCAPE '\\' OR e.excerpt LIKE ? ESCAPE '\\' OR d.title LIKE ? ESCAPE '\\')"]
            params: list[Any] = [sql_like(q)]*3
            if domain:
                where.append("d.domain=?"); params.append(domain)
            if kind:
                where.append("e.kind=?");params.append(kind)
            rows = con.execute("""SELECT e.id,e.document_id,e.kind,e.subtype,e.title,e.excerpt,e.start_line,
                                       d.title AS module_title,d.domain
                                 FROM entities e JOIN documents d ON d.id=e.document_id
                                 WHERE """+" AND ".join(where)+" ORDER BY CASE WHEN e.title LIKE ? ESCAPE '\\' THEN 0 ELSE 1 END, e.kind,e.document_id,e.start_offset LIMIT ?",
                                (*params,sql_like(q),limit)).fetchall()
            results.extend(dict(x) for x in rows)
        # Full-document FTS5 searches all TeX content, not just the first excerpt.
        if kind in (None,"module") and len(results)<limit:
            remaining=limit-len(results)
            try:
                expr='"'+q.replace('"','""')+'"'
                sql="""SELECT d.id,d.title,d.domain,
                                snippet(document_fts,3,'[',']','…',16) AS excerpt
                         FROM document_fts JOIN documents d ON d.id=document_fts.document_id
                         WHERE document_fts MATCH ?"""
                args: list[Any]=[expr]
                if domain:
                    sql+=" AND d.domain=?";args.append(domain)
                sql+=" LIMIT ?";args.append(remaining)
                documents=con.execute(sql,args).fetchall()
            except sqlite3.OperationalError:
                sql="SELECT id,title,domain,substr(content,1,240) AS excerpt FROM documents WHERE content LIKE ? ESCAPE '\\'"
                args=[sql_like(q)]
                if domain:
                    sql+=" AND domain=?";args.append(domain)
                sql+=" LIMIT ?";args.append(remaining)
                documents=con.execute(sql,args).fetchall()
            for doc in documents:
                results.append({"id":doc["id"],"document_id":doc["id"],"kind":"module",
                                "subtype":"module","title":doc["title"],"excerpt":doc["excerpt"],
                                "start_line":1,"module_title":doc["title"],"domain":doc["domain"]})
        return {"items":results, "query":q,"limit":limit}


class Selection(BaseModel):
    modules: list[str] = Field(default_factory=list,max_length=300)
    entities: list[str] = Field(default_factory=list,max_length=300)


@app.post("/api/selection/plan")
def selection_plan(selection: Selection):
    with db_connection() as con:
        doc_ids = list(dict.fromkeys(selection.modules))
        selected_entities = []
        unknown_entities = []
        for eid in dict.fromkeys(selection.entities):
            r=con.execute("SELECT id,document_id,kind,title,start_line FROM entities WHERE id=?",(eid,)).fetchone()
            if r:
                selected_entities.append(dict(r))
                if r["document_id"] not in doc_ids:
                    doc_ids.append(r["document_id"])
            else:
                unknown_entities.append(eid)
        plan=analyze_selection(con,doc_ids)
        plan["selected_entities"] = selected_entities
        plan["unknown_entities"] = unknown_entities
        # Whole-module plan overestimates dependencies if only fragments are selected.
        plan["fragment_scope_warning"] = bool(selected_entities)
        plan["status"] = "preliminary" if selected_entities else "module-complete"
        plan["compilation_performed"] = False
        return plan


def bipartite_graph(con: sqlite3.Connection, left: str, right: str,
                    granularity: str, min_weight:int, max_edges: int) -> dict[str,Any]:
    # The only input relationships are *explicit* TeX references; there is no inferred semantics.
    docs = {r["id"]:dict(r) for r in con.execute("SELECT id,title,domain FROM documents")}
    if left not in {r["domain"] for r in docs.values()} or right not in {r["domain"] for r in docs.values()}:
        raise HTTPException(status_code=400,detail="Nieznana dziedzina.")
    rows=con.execute("""SELECT source_document,source_entity,target_document,target_entity,target_label
                        FROM references_tex WHERE status IN ('resolved','external_resolved','alias_resolved') AND target_document IS NOT NULL
                          AND source_document!=target_document""").fetchall()
    owners={}
    if granularity == "section":
        entities={r["id"]:dict(r) for r in con.execute("SELECT id,parent_id,kind,title,document_id FROM entities")}
        heads={"chapter","section","subsection","subsubsection","paragraph","part"}
        def section_owner(entity_id,docid):
            key=(entity_id,docid)
            if key in owners: return owners[key]
            original=entity_id;seen=set()
            while entity_id and entity_id in entities and entity_id not in seen:
                seen.add(entity_id)
                e=entities[entity_id]
                if e["kind"] in heads:
                    owners[key]=(e["id"],e["title"],e["kind"])
                    return owners[key]
                entity_id=e["parent_id"]
            owners[key]=(docid,docs[docid]["title"],"module")
            return owners[key]
    elif granularity == "entity":
        entities={r["id"]:dict(r) for r in con.execute("SELECT id,parent_id,kind,title,document_id FROM entities")}
        def section_owner(entity_id,docid):
            if entity_id in entities:
                e=entities[entity_id];return e["id"],e["title"] or e["kind"],e["kind"]
            return docid,docs[docid]["title"],"module"
    else:
        def section_owner(entity_id,docid):
            return docid,docs[docid]["title"],"module"
    # Create side-specific nodes for actual bipartiteness even when both filters are identical.
    counts:Counter[tuple[str,str]]=Counter()
    nodes: dict[str,dict[str,Any]]={}
    for r in rows:
        s,d=r["source_document"],r["target_document"]
        if docs[s]["domain"]==left and docs[d]["domain"]==right:
            leftdoc,rightdoc=s,d;le=r["source_entity"];re=r["target_entity"]
        elif docs[d]["domain"]==left and docs[s]["domain"]==right:
            leftdoc,rightdoc=d,s;le=r["target_entity"];re=r["source_entity"]
        else:continue
        a,ta,ka=section_owner(le,leftdoc)
        b,tb,kb=section_owner(re,rightdoc)
        aid,bid="L:"+a,"R:"+b
        nodes.setdefault(aid,{"id":aid,"entity_id":a,"module":leftdoc,"label":ta,"kind":ka,"side":"left","domain":left})
        nodes.setdefault(bid,{"id":bid,"entity_id":b,"module":rightdoc,"label":tb,"kind":kb,"side":"right","domain":right})
        counts[(aid,bid)]+=1
    ordered=[(a,b,w) for (a,b),w in sorted(counts.items(),key=lambda kv:(-kv[1],kv[0])) if w>=min_weight]
    truncated=len(ordered)>max_edges
    selected=ordered[:max_edges]
    node_ids={id for a,b,_ in selected for id in (a,b)}
    final_nodes=sorted((v for k,v in nodes.items() if k in node_ids),key=lambda x:(x["side"],x["module"],x["id"]))
    edges=[{"source":a,"target":b,"weight":w} for a,b,w in selected]
    return {"bipartite":True,"evidence":"explicit_tex_references","granularity":granularity,
            "left":left,"right":right,"nodes":final_nodes,"edges":edges,"truncated":truncated,
            "available_edges":len(ordered)}


@app.get("/api/concepts/graph")
def concept_occurrence_graph(
    q: Annotated[str, Query(min_length=2, max_length=100)],
    max_occurrences: Annotated[int, Query(ge=1, le=80)] = 36,
):
    """Grounded concept graph: actual TeX occurrences plus curated relations."""
    with db_connection() as con:
        return build_concept_graph(con, q, max_occurrences)


@app.get("/api/graph")
def graph(left: str, right: str, granularity: Literal["module","section","entity"]="module",
          min_weight:Annotated[int,Query(ge=1,le=100)]=1,
          max_edges:Annotated[int,Query(ge=1,le=250)]=90):
    with db_connection() as con:
        return bipartite_graph(con,left,right,granularity,min_weight,max_edges)


@app.get("/api/graph/path")
def graph_path(source: str, target: str):
    with db_connection() as con:
        require_document(con,source);require_document(con,target)
        G=nx.Graph()
        for r in con.execute("SELECT source_document,target_document,references_count FROM dependency_edges WHERE source_document!=target_document"):
            a,b=r["source_document"],r["target_document"]
            if G.has_edge(a,b):G[a][b]["weight"]+=r["references_count"]
            else:G.add_edge(a,b,weight=r["references_count"])
        try:
            path=nx.shortest_path(G,source,target)
        except (nx.NodeNotFound,nx.NetworkXNoPath):
            return {"found":False,"modules":[],"steps":[],"relation":"undirected_explicit_references"}
        details={r["id"]:r["title"] for r in con.execute("SELECT id,title FROM documents")}
        return {"found":True,"modules":[{"id":x,"title":details[x]} for x in path],
                "steps":[{"source":a,"target":b,"weight":G[a][b]["weight"]} for a,b in zip(path,path[1:])],
                "relation":"undirected_explicit_references","direction_ignored":True}

# Generator API: no canonical .tex or SQLite writes, no shell execution.
class CustomItem(BaseModel):
    kind: Literal["module", "entity", "lines"]
    id: str | None = Field(default=None, max_length=300)
    module: str | None = Field(default=None, max_length=100)
    start_line: int | None = None
    end_line: int | None = None


class GenerateRequest(BaseModel):
    title: str = Field(default='Mój skrypt matematyczny',min_length=1,max_length=160)
    modules: list[str] = Field(default_factory=list,max_length=75)
    entities: list[str] = Field(default_factory=list,max_length=300)
    items: list[CustomItem] | None = Field(default=None,max_length=300)
    closure_depth: int = Field(default=0,ge=0,le=3)


@app.post('/api/generate')
def generate_project_endpoint(selection: GenerateRequest):
    from fastapi.responses import Response
    from backend.generator import GenerationError, project_files, zip_project
    try:
        with db_connection() as con:
            files,manifest=project_files(con,selection.modules,selection.entities,selection.title,selection.closure_depth,
                                     items=([item.model_dump(exclude_none=True) for item in selection.items] if selection.items is not None else None))
        archive=zip_project(files)
    except GenerationError as exc:
        raise HTTPException(status_code=422,detail=str(exc)) from exc
    return Response(content=archive,media_type='application/zip',headers={
        'Content-Disposition':'attachment; filename="skrypt_matematyczny.zip"',
        'X-Matlib-Modules':str(len(manifest['modules'])),
        'X-Matlib-External-Refs':str(manifest['references_external'])})


@app.post('/api/generate/manifest')
def generate_manifest_endpoint(selection: GenerateRequest):
    from backend.generator import GenerationError, project_files
    try:
        with db_connection() as con:
            _,manifest=project_files(con,selection.modules,selection.entities,selection.title,selection.closure_depth,
                                     items=([item.model_dump(exclude_none=True) for item in selection.items] if selection.items is not None else None))
        return manifest
    except GenerationError as exc:
        raise HTTPException(status_code=422,detail=str(exc)) from exc


# Browser-tab drafts: explicit save persists; closing X discards unsaved work.
@app.post('/api/drafts')
def create_draft(selection: GenerateRequest, session_id: str | None = None):
    from backend.generator import GenerationError, project_files, zip_project
    try:
        with db_connection() as con:
            files, manifest = project_files(con, selection.modules, selection.entities, selection.title, selection.closure_depth,
                                            items=([item.model_dump(exclude_none=True) for item in selection.items] if selection.items is not None else None))
        return workspaces.stage_project(zip_project(files), manifest, session_id)
    except (GenerationError, workspaces.WorkspaceError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get('/api/drafts/{session_id}/download')
def download_draft(session_id: str):
    try:
        archive = workspaces.get_draft_archive(session_id)
    except workspaces.WorkspaceError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return FileResponse(archive, media_type='application/zip', filename='mathematical_draft.zip')


@app.post('/api/drafts/{session_id}/save')
def persist_draft(session_id: str):
    try:
        return workspaces.save_draft(session_id)
    except workspaces.WorkspaceError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post('/api/drafts/{session_id}/close')
def discard_draft(session_id: str):
    try:
        return {'removed': workspaces.close_draft(session_id)}
    except workspaces.WorkspaceError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get('/api/projects')
def saved_projects():
    return {'items': workspaces.list_saved_projects()}


@app.get('/api/projects/{project_id}/download')
def download_saved_project(project_id: str):
    try:
        archive = workspaces.get_saved_archive(project_id)
    except workspaces.WorkspaceError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return FileResponse(archive, media_type='application/zip', filename='saved_mathematical_project.zip')


@app.post('/api/drafts/{session_id}/heartbeat')
def keep_draft_alive(session_id: str):
    try:
        workspaces.get_draft_archive(session_id)
        return {'active': True}
    except workspaces.WorkspaceError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
