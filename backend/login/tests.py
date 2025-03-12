from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from login.models import CompanyUser

class UserModelTest(TestCase):
    def test_create_user(self):
        user = CompanyUser.objects.create_user(username='testuser', password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password123'))
    
    def test_create_superuser(self):
        superuser = CompanyUser.objects.create_superuser(username='admin', password='adminpassword')
        self.assertEqual(superuser.username, 'admin')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.check_password('adminpassword'))
