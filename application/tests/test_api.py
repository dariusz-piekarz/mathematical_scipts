"""End-to-end HTTP tests against the bundled library snapshot, no network required."""
import unittest
from fastapi.testclient import TestClient
from backend.api import app, db_connection


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client_context = TestClient(app)
        cls.client = cls._client_context.__enter__()

    @classmethod
    def tearDownClass(cls):
        cls._client_context.__exit__(None, None, None)

    def test_frontend(self):
        r=self.client.get("/")
        self.assertEqual(r.status_code,200)
        self.assertIn("Explorer",r.text)
        for name in ("app.js","styles.css"):
            self.assertEqual(self.client.get("/assets/"+name).status_code,200)

    def test_health(self):
        self.assertTrue(self.client.get("/api/health").json()["readonly"])

    def test_stats(self):
        data=self.client.get("/api/stats").json()
        self.assertGreaterEqual(data["documents"],350)
        self.assertGreaterEqual(data["references"],4400)
        self.assertGreaterEqual(data["ambiguous_references"],0)
        with db_connection() as con:
            count = con.execute("SELECT COUNT(*) FROM label_occurrences").fetchone()[0]
            conflicts = con.execute("SELECT COUNT(DISTINCT name) FROM label_conflicts").fetchone()[0]
        self.assertGreater(count,0)
        self.assertGreater(conflicts,0)  # conflicts are preserved as provenance even when refs resolve
        self.assertGreaterEqual(data["missing_references"],0)

    def test_measure_theory_and_jets_available(self):
        result=self.client.get("/api/modules/ME-31")
        self.assertEqual(result.status_code,200)
        self.assertIn("Dżety",result.json()["module"]["title"])
        self.assertIn("teoria miary",result.json()["module"]["domain"])

    def test_domains(self):
        data=self.client.get("/api/domains").json()
        self.assertGreaterEqual(sum(x["modules"] for x in data),350)
        self.assertIn("geometria algebraiczna",{x["name"] for x in data})

    def test_modules(self):
        res=self.client.get("/api/modules?domain=geometria%20algebraiczna")
        self.assertEqual(res.status_code,200)
        self.assertTrue(all(x["domain"]=="geometria algebraiczna" for x in res.json()["items"]))

    def test_search_modules_by_id(self):
        res=self.client.get("/api/modules?q=ALG-09")
        self.assertEqual(res.json()["total"],1)

    def test_module(self):
        res=self.client.get("/api/modules/ALG-09")
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.json()["module"]["id"],"ALG-09")
        self.assertIn("\\chapter",res.json()["latex"])

    def test_unknown_module(self):
        self.assertEqual(self.client.get("/api/modules/THIS_MODULE_DOES_NOT_EXIST").status_code,404)

    def test_outline(self):
        data=self.client.get("/api/modules/ALG-09/outline").json()
        self.assertTrue(any(x["kind"]=="chapter" for x in data["entities"]))
        self.assertTrue(any(x["kind"]=="theorem" for x in data["entities"]))

    def test_entity(self):
        e=self.client.get("/api/entities/label:ch:pierscienie").json()
        self.assertEqual(e["entity"]["document_id"],"ALG-00")
        self.assertIn("\\chapter",e["latex"])
        self.assertTrue(e["truncated"])

    def test_labels(self):
        item=self.client.get("/api/labels/ch:pierscienie").json()
        self.assertEqual(item["document_id"],"ALG-00")
        self.assertIn("incoming_references",item)
        self.assertEqual(self.client.get("/api/labels/not:existing").status_code,404)

    def test_search(self):
        data=self.client.get("/api/search",params={"q":"Lefschetza","limit":10}).json()
        self.assertGreater(len(data["items"]),0)
        self.assertTrue(any(x["kind"] for x in data["items"]))

    @classmethod
    def _real_reference_domains(cls):
        """Use a proven explicit cross-module TeX reference from the indexed corpus.

        The old fixed pair stopped being related after chapter reorganization.
        This keeps the HTTP graph contract tested without inventing links.
        """
        with db_connection() as con:
            row = con.execute("""
                SELECT s.domain AS left_domain, t.domain AS right_domain
                FROM references_tex AS r
                JOIN documents AS s ON s.id=r.source_document
                JOIN documents AS t ON t.id=r.target_document
                WHERE r.status='resolved' AND r.target_document IS NOT NULL
                  AND r.source_document!=r.target_document
                GROUP BY s.domain, t.domain
                ORDER BY COUNT(*) DESC, s.domain, t.domain
                LIMIT 1
            """).fetchone()
        if row is None:
            raise AssertionError("Index has no resolved cross-module TeX references")
        return {"left":row["left_domain"], "right":row["right_domain"]}

    @classmethod
    def _real_dependency_edge(cls):
        with db_connection() as con:
            row=con.execute("""
                SELECT source_document, target_document
                FROM dependency_edges
                WHERE source_document!=target_document
                ORDER BY references_count DESC, source_document, target_document
                LIMIT 1
            """).fetchone()
        if row is None:
            raise AssertionError("Index has no cross-module dependency edges")
        return {"source":row["source_document"],"target":row["target_document"]}

    def test_graph_bipartite(self):
        params=self._real_reference_domains()
        data=self.client.get("/api/graph",params=params).json()
        self.assertTrue(data["bipartite"])
        self.assertGreater(len(data["edges"]),0)
        groups={n["id"]:n["side"] for n in data["nodes"]}
        for e in data["edges"]:
            self.assertEqual((groups[e["source"]],groups[e["target"]]),("left","right"))

    def test_graph_section(self):
        params={**self._real_reference_domains(),"granularity":"section"}
        data=self.client.get("/api/graph",params=params).json()
        self.assertGreater(len(data["edges"]),0)

    def test_graph_entity(self):
        params={**self._real_reference_domains(),"granularity":"entity"}
        data=self.client.get("/api/graph",params=params).json()
        self.assertGreater(len(data["edges"]),0)

    def test_graph_missing_pair(self):
        params={"left":"geometria algebraiczna","right":"topologia algebraiczna"}
        data=self.client.get("/api/graph",params=params).json()
        self.assertEqual(data["edges"],[])

    def test_graph_bad_domain(self):
        params={"left":"nonsense","right":"topologia algebraiczna"}
        self.assertEqual(self.client.get("/api/graph",params=params).status_code,400)

    def test_graph_path(self):
        params=self._real_dependency_edge()
        response=self.client.get("/api/graph/path",params=params)
        self.assertEqual(response.status_code,200,response.text)
        data=response.json()
        self.assertTrue(data["found"])
        self.assertEqual(data["modules"][0]["id"],params["source"])

    def test_plan(self):
        data=self.client.post("/api/selection/plan",json={"modules":["ALG-09"]}).json()
        self.assertTrue(data["requires_xr_hyper"])
        self.assertGreater(data["external_references"],0)
        self.assertFalse(data["compilation_performed"])

    def test_fragment_plan_preliminary(self):
        data=self.client.post("/api/selection/plan",json={"entities":["label:ch:pierscienie"]}).json()
        self.assertTrue(data["fragment_scope_warning"])
        self.assertEqual(data["status"],"preliminary")

    def test_untrusted_search_characters(self):
        self.assertEqual(self.client.get("/api/search",params={"q":"100%_'\\"}).status_code,200)

    def test_query_limits(self):
        self.assertEqual(self.client.get("/api/modules",params={"limit":1000}).status_code,422)
        self.assertEqual(self.client.get("/api/search",params={"q":""}).status_code,422)


if __name__ == "__main__":
    unittest.main()