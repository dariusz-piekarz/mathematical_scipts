"""End-to-end HTTP tests against the bundled library snapshot, no network required."""
import unittest
from fastapi.testclient import TestClient
from backend.api import app


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

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
        self.assertEqual((data["documents"],data["labels"],data["references"]),(233,2363,1515))
        self.assertEqual(data["missing_references"],0)

    def test_domains(self):
        data=self.client.get("/api/domains").json()
        self.assertEqual(sum(x["modules"] for x in data),233)
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
        self.assertEqual(self.client.get("/api/modules/TOP-28").status_code,404)

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

    def test_graph_bipartite(self):
        params={"left":"geometria algebraiczna","right":"geometria algebraiczna / topologia"}
        data=self.client.get("/api/graph",params=params).json()
        self.assertTrue(data["bipartite"])
        self.assertGreater(len(data["edges"]),0)
        groups={n["id"]:n["side"] for n in data["nodes"]}
        for e in data["edges"]:
            self.assertEqual((groups[e["source"]],groups[e["target"]]),("left","right"))

    def test_graph_section(self):
        params={"left":"geometria algebraiczna","right":"geometria algebraiczna / topologia","granularity":"section"}
        data=self.client.get("/api/graph",params=params).json()
        self.assertGreater(len(data["edges"]),0)

    def test_graph_entity(self):
        params={"left":"geometria algebraiczna","right":"geometria algebraiczna / topologia","granularity":"entity"}
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
        data=self.client.get("/api/graph/path",params={"source":"ALG-09","target":"AT-10"}).json()
        self.assertTrue(data["found"])
        self.assertEqual(data["modules"][0]["id"],"ALG-09")

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
