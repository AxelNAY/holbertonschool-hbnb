import unittest
import json
from app import app

class UserApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users/', 
                                 data=json.dumps(dict(email="test@example.com", password="password123", first_name="John", last_name="Doe", status="host")),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.app.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.app.post('/users/', 
                                 data=json.dumps(dict(email="unique@example.com", password="password123", first_name="Jane", last_name="Doe", status="commenter")),
                                 content_type='application/json')
        user_id = response.json['id']
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.app.post('/users/', 
                                 data=json.dumps(dict(email="update@example.com", password="password123", first_name="Jane", last_name="Doe", status="commenter")),
                                 content_type='application/json')
        user_id = response.json['id']
        response = self.app.put(f'/users/{user_id}', 
                                data=json.dumps(dict(first_name="Janet")),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.app.post('/users/', 
                                 data=json.dumps(dict(email="delete@example.com", password="password123", first_name="John", last_name="Doe", status="host")),
                                 content_type='application/json')
        user_id = response.json['id']
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

