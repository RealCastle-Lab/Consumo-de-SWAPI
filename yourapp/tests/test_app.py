# tests/test_app.py
import unittest
from app import create_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Setup the Flask app for testing."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_home_page(self):
        """Test that the home page loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bienvenido', response.data.decode())

    def test_about_page(self):
        """Test that the about page loads correctly."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Acerca de la Aplicación', response.data.decode())

if __name__ == '__main__':
    unittest.main()
