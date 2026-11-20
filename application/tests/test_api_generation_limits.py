"""HTTP boundary and rejection tests for generation endpoints."""
import unittest
from fastapi.testclient import TestClient
from backend.api import app

class GenerationAPILimits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = TestClient(app)
        cls.client = cls.context.__enter__()

    @classmethod
    def tearDownClass(cls):
        cls.context.__exit__(None, None, None)

    def test_request_boundaries(self):
        base={'modules':['ALG-09']}
        for field, value in [('modules',['ALG-09']*76),('entities',['x']*301),('closure_depth',4),('closure_depth',-1),('title','x'*161),('title','')]:
            response=self.client.post('/api/generate/manifest',json={**base,field:value})
            self.assertEqual(response.status_code,422,(field,response.text[:300]))

    def test_invalid_selections_are_rejected_without_server_error(self):
        for endpoint in ('/api/generate','/api/generate/manifest','/api/drafts'):
            response=self.client.post(endpoint,json={'modules':['NO-SUCH-MODULE']})
            self.assertEqual(response.status_code,422,(endpoint,response.text[:300]))

    def test_real_archive_http_contract(self):
        response=self.client.post('/api/generate',json={'modules':['ALG-09']})
        self.assertEqual(response.status_code,200,response.text[:300] if response.status_code!=200 else '')
        self.assertEqual(response.headers['content-type'],'application/zip')
        self.assertLessEqual(len(response.content),64*1024*1024)
        import io,zipfile
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            self.assertIsNone(z.testzip())
            self.assertIn('main.tex',z.namelist())

if __name__=='__main__': unittest.main()