import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.client = app.test_client()

    def test_analyze_positive(self):
        response = self.client.post("/analyze", json={"text": "I love this project!"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("sentiment", data)
        self.assertEqual(data["sentiment"], "positive")

    def test_analyze_negative(self):
        response = self.client.post("/analyze", json={"text": "I hate bugs."})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("sentiment", data)
        self.assertEqual(data["sentiment"], "negative")

    def test_analyze_neutral(self):
        response = self.client.post("/analyze", json={"text": "The sky is blue."})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("sentiment", data)
        self.assertEqual(data["sentiment"], "neutral")

    def test_analyze_no_text(self):
        response = self.client.post("/analyze", json={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()
