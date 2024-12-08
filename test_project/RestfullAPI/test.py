# test_user_management.py

import unittest
import json
from user_management import app

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_user(self):
        response = self.client.post('/users', json={"id": 1, "name": "Alice", "email": "alice@example.com"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Alice", response.get_data(as_text=True))

    def test_get_users(self):
        self.client.post('/users', json={"id": 1, "name": "Alice", "email": "alice@example.com"})
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alice", response.get_data(as_text=True))

    def test_get_user(self):
        self.client.post('/users', json={"id": 1, "name": "Alice", "email": "alice@example.com"})
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alice", response.get_data(as_text=True))

    def test_delete_user(self):
        self.client.post('/users', json={"id": 1, "name": "Alice", "email": "alice@example.com"})
        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("User deleted", response.get_data(as_text=True))
