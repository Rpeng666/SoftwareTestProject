import unittest
import json
from app import app, users_db

class TestUserManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.username = 'testuser1'
        cls.email = 'testuser1@example.com'

    def setUp(self):
        # 清理测试环境
        users_db.clear()

    def test_create_user_success(self):
        response = self.client.post(
            '/users',
            data=json.dumps({
                'username': self.username,
                'email': self.email
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(self.username, users_db)

    def test_create_user_failure_duplicate(self):
        self.test_create_user_success()
        response = self.client.post(
            '/users',
            data=json.dumps({
                'username': self.username,
                'email': self.email
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)
        self.assertIn("User already exists", response.json['error'])

    def test_get_all_users(self):
        self.test_create_user_success()
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertEqual(len(response.json), 1)
        self.assertIn(self.username, str(response.data))

    def test_get_user_success(self):
        self.test_create_user_success()
        response = self.client.get(f'/users/{self.username}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.username, str(response.data))

    def test_get_user_failure_not_found(self):
        response = self.client.get('/users/nonexistentuser')
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found", response.json['error'])

    def test_delete_user_success(self):
        self.test_create_user_success()
        response = self.client.delete(f'/users/{self.username}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("User deleted", response.json['message'])
        self.assertNotIn(self.username, users_db)

    def test_delete_user_failure_not_found(self):
        response = self.client.delete('/users/nonexistentuser')
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found", response.json['error'])

if __name__ == '__main__':
    unittest.main()
