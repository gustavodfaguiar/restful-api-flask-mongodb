import json
import unittest
from unittest import mock
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valid_return_all_language(self):
        langs = {
            "languages": [
                {
                "_id": "5f581d69af78f0e77eedcef9",
                "name": "Python"
                }
            ]
        }
        response = self.client.get("/lang", json=langs)
        data = json.loads(response.data.decode())
        self.assertEqual(data["languages"][0]["name"], "Python")
