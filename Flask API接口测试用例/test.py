import unittest
import json
import os
import sys
# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取上一级目录
parent_dir = os.path.dirname(current_dir)

# 将上一级目录添加到 sys.path 中
sys.path.append(parent_dir)
from test_project.RestfullAPI.main import app, users

class TestUserManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_client = app.test_client()

    def setUp(self):
        # 清空users字典，确保每次测试开始时是干净的
        users.clear()

    def test_create_user_success(self):
        response = self.test_client.post(
            '/users',
            data=json.dumps({"id": 1, "name": "John Doe", "email": "john@example.com"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(1, users)
        self.assertDictEqual(users[1], {"name": "John Doe", "email": "john@example.com"})

    def test_create_user_failure_duplicate_id(self):
        self.test_client.post(
            '/users',
            data=json.dumps({"id": 2, "name": "Jane Doe", "email": "jane@example.com"}),
            content_type='application/json'
        )
        response = self.test_client.post(
            '/users',
            data=json.dumps({"id": 2, "name": "Another Jane Doe", "email": "another_jane@example.com"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", json.loads(response.data))

    def test_get_all_users(self):
        self.test_client.post(
            '/users',
            data=json.dumps({"id": 3, "name": "Alice Smith", "email": "alice@example.com"}),
            content_type='application/json'
        )
        response = self.test_client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), {3: {"name": "Alice Smith", "email": "alice@example.com"}})

    def test_get_single_user_success(self):
        self.test_client.post(
            '/users',
            data=json.dumps({"id": 4, "name": "Bob Brown", "email": "bob@example.com"}),
            content_type='application/json'
        )
        response = self.test_client.get('/users/4')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), {"name": "Bob Brown", "email": "bob@example.com"})

    def test_get_single_user_failure_not_found(self):
        response = self.test_client.get('/users/5')
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", json.loads(response.data))

    def test_delete_user_success(self):
        self.test_client.post(
            '/users',
            data=json.dumps({"id": 6, "name": "Charlie Chan", "email": "charlie@example.com"}),
            content_type='application/json'
        )
        response = self.test_client.delete('/users/6')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(6, users)

    def test_delete_user_failure_not_found(self):
        response = self.test_client.delete('/users/7')
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", json.loads(response.data))

if __name__ == '__main__':
    unittest.main()
