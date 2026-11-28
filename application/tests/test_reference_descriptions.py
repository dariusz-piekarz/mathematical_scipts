"""Descriptions and navigation must use the same label resolution rules."""
import unittest
from fastapi.testclient import TestClient
from backend.api import app, db_connection


class ReferenceDescriptionsTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_descriptions_match_navigation(self):
        labels = ['ch:ga5-rozdmuchania', 'AA-37::aa:tw:transcendence-degree']
        response = self.client.post('/api/references/descriptions', json={'source_document': 'ALG-08', 'labels': labels})
        self.assertEqual(response.status_code, 200)
        for label in labels:
            description = response.json()['items'][label]
            detail = self.client.get('/api/labels/' + label, params={'source_document': 'ALG-08'}).json()
            self.assertEqual(description['document_id'], detail['document_id'])
            self.assertEqual(description['entity_id'], detail['entity_id'])
            self.assertNotIn('latex', description)
        self.assertIn('Rozdmuchania', response.json()['items'][labels[0]]['entity_title'])

    def test_missing_qualified_target_does_not_fall_back(self):
        label = 'ALG-08::ch:ga5-rozdmuchania'
        items = self.client.post('/api/references/descriptions', json={'labels': [label]}).json()['items']
        self.assertTrue(items[label]['missing'])

    def test_conflicts_remain_explicit(self):
        with db_connection() as con:
            label = con.execute('SELECT name FROM label_conflicts ORDER BY name LIMIT 1').fetchone()[0]
        result = self.client.post('/api/references/descriptions', json={'labels': [label]}).json()['items'][label]
        self.assertTrue(result['ambiguous'])
        for candidate in result['candidates']:
            response = self.client.get('/api/labels/' + candidate['document_id'] + '::' + label)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['entity_id'], candidate['entity_id'])


if __name__ == '__main__':
    unittest.main()
