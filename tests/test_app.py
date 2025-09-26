import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        print("\n🔧 Setting up test client...")

    def test_analyze_positive(self):
        print("➡️ Testing positive sentiment...")
        response = self.client.post("/analyze", json={"text": "I love this project!"})
        print("Response JSON:", response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["sentiment"], "positive")

    def test_analyze_negative(self):
        print("➡️ Testing negative sentiment...")
        response = self.client.post("/analyze", json={"text": "I hate bugs."})
        print("Response JSON:", response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["sentiment"], "negative")

    def test_analyze_neutral(self):
        print("➡️ Testing neutral sentiment...")
        response = self.client.post("/analyze", json={"text": "The sky is blue."})
        print("Response JSON:", response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["sentiment"], "neutral")

    def test_analyze_no_text(self):
        print("➡️ Testing missing text error...")
        response = self.client.post("/analyze", json={})
        print("Response JSON:", response.get_json())
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main(verbosity=2)
