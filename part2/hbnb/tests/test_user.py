import unittest
from app import create_app

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        res = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@test.com"
        })
        self.assertEqual(res.status_code, 201)

    def test_invalid_user(self):
        res = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "bad"
        })
        self.assertEqual(res.status_code, 400)