import unittest
from unittest import TestCase
from app import app

class FlaskRoutesTest(TestCase):
    # This creates setup logic and enables other tests to be run
    def setUp(self):
        self.client = app.test_client()
        # configures the client to run in testing mode
        self.client.testing = True
    
    def test_index_route(self):
        response = self.client.get('/')
        # checks if response is equal to 200 (good response)
        self.assertEqual(response.status_code, 200, 'Expected a 200 response')
        print('test_index_route: Success! Received a 200 response')
        # checks the response data is correct
        self.assertIn(b'Welcome to the Vetinary Practice Booking System', response.data, 'Expected "Welcome to the Vetinary Practice Booking System" in response')
        print('test_index_route: Success! Correct data receieved')

    
if __name__ == '__main__':
    unittest.main()


