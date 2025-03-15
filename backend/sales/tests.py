from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Lead, Deal


class LeadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lead_data = {
            'company': 1,
            'name': 'Test Lead',
            'email': 'test@example.com',
            'phone': '1234567890',
        }

    def test_create_lead(self):
        response = self.client.post('/sales/leads/create/', self.lead_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_leads(self):
        Lead.objects.create(**self.lead_data)
        response = self.client.get('/sales/leads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DealTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.deal_data = {
            'lead_id': 1,
            'value': 1000,
            'stage': 'prospecting',
        }

    def test_create_deal(self):
        response = self.client.post('/sales/deals/create/', self.deal_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
