from django.test import TestCase
from django.test import Client

class PageTest(TestCase):
    def test_page_landing(self):
        c = Client()
        response = c.get('')
        self.assertEqual(response.status_code, 200)
        
    def test_page_post(self):
        c = Client()
        response = c.post('')
        self.assertEqual(response.status_code, 200)