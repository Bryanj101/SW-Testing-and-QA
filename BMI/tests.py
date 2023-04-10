from django.test import TestCase, LiveServerTestCase
from django.test import Client

class PageTest(LiveServerTestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_page_landing(self):
        c = Client()
        response = c.get('')
        self.assertEqual(response.status_code, 200)
        
    def test_page_post(self):
        c = Client()
        response = c.post('')
        self.assertEqual(response.status_code, 200)
    
    def testform(self):
        c = Client()
        response = c.post('', {'weight': 60, 'height': 17})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['bmi'], 149.5)