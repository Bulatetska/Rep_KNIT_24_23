import unittest
import json
from app import app

class ProfilesTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_profiles_empty(self):
        # Test GET request to /profiles when there are no profiles
        response = self.client.get('/profiles')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data), 0)

    def test_post_profile(self):
        # Test POST request to /profiles to add a new profile
        profile_data = {
            'name': 'John Doe',
            'category': 'test',
            'rating': 5
        }
        response = self.client.post('/profiles', json=profile_data)
        self.assertEqual(response.status_code, 200)

    def test_get_profiles(self):
        # Test GET request to /profiles to retrieve profiles
        response = self.client.get('/profiles')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
       # self.assertEqual(len(data), 1)

    def test_get_calculations(self):
        # Test GET request to /calculations to retrieve calculations
        response = self.client.get('/calculations')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('total_profiles', data)
        self.assertIn('total_rating', data)
        self.assertIn('average_rating', data)
        self.assertIn('category_ratings', data)
        self.assertIn('category_min_profiles', data)
        self.assertIn('category_max_profiles', data)

if __name__ == '__main__':
    unittest.main()
