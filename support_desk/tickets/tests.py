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

    def test_ticket_list_pagination(self):
        """Pagination should return http ok for success access"""
        response = self.client.get('http://127.0.0.1:8000/?page=1')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_ticket_list_pagination_not_found(self):
        """Pagination should return http ok when entering invalid page manually"""
        response = self.client.get('http://127.0.0.1:8000/?page=5ss')
        self.assertEqual(response.status_code, 200)

    def test_access_ticket_not_found(self):
        """The invalid ticket id should return 404 status"""
        response = self.client.get('http://127.0.0.1:8000/view/1dsd')
        self.assertEqual(response.status_code, 404)