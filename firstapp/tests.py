try:
    import json
except:
    import simplejson as json
from django.test import TestCase


class HomePageTest(TestCase):
    

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('info' in response.context)


class RequestTest(TestCase):
    def test_requests(self):
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('request' in response.context)

