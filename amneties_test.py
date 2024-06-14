# test_app.py
import unittest
from app import app, Amneties

class AmenitiesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        Amneties.amneties_object_list = []
        Amneties.amnetie_count = 0

    def test_create_amenity(self):
        response = self.app.post('/amenities', json={'name': 'Pool'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Pool')

    def test_create_duplicate_amenity(self):
        self.app.post('/amenities', json={'name': 'Pool'})
        response = self.app.post('/amenities', json={'name': 'Pool'})
        self.assertEqual(response.status_code, 409)

    def test_get_amenities(self):
        self.app.post('/amenities', json={'name': 'Pool'})
        response = self.app.get('/amenities')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_get_specific_amenity(self):
        post_response = self.app.post('/amenities', json={'name': 'Pool'})
        amenity_id = post_response.json['_Amneties__id']
        response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Pool')

    def test_update_amenity(self):
        post_response = self.app.post('/amenities', json={'name': 'Pool'})
        amenity_id = post_response.json['_Amneties__id']
        response = self.app.put(f'/amenities/{amenity_id}', json={'name': 'Gym'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Gym')

    def test_delete_amenity(self):
        post_response = self.app.post('/amenities', json={'name': 'Pool'})
        amenity_id = post_response.json['_Amneties__id']
        response = self.app.delete(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)
        get_response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

