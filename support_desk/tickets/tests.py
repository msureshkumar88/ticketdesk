from django.test import TestCase
from django.urls import reverse
from django.conf import settings

# Create your tests here.
class TicketTestCase(TestCase):
    def test_access_ticket_list(self):
        """The site is not running"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_access_ticket_single(self):
        """The connect ticket id should return http ok"""
        response = self.client.get('http://127.0.0.1:8000/view/223')
        self.assertEqual(response.status_code, 200)

    def test_access_ticket_not_found(self):
        """The invalid ticket id should return 404 status"""
        response = self.client.get('http://127.0.0.1:8000/view/1')
        self.assertEqual(response.status_code, 404)

    def test_api_not_connected(self):
        """Connection with Zendesk not success 500 status should return"""
        settings.AUTH_USER = "test"
        settings.AUTH_PASS = "test"
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 500)

