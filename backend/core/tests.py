from django.test import TestCase
from rest_framework.test import APITestCase
from login.models import CompanyUser

class AuthenticationTestCase(APITestCase):

    # def test_obter_token_jwt(self):
    #     user = CompanyUser.objects.create_user(username='testuser', password='password123')
    #     response = self.client.post("/token/", {"username": "testuser", "password": "password123"})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("access", response.data)

    def test_fail_obter_token_jwt(self):
        user = CompanyUser.objects.create_user(username='testuser', password='password123')
        response = self.client.post("/token/", {"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, 404)
