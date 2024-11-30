from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'role': 'student',
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post('/api/users/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
