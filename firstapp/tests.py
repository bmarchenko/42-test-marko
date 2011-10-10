from django.test import TestCase
from django.core.urlresolvers import reverse

class HomePageTest(TestCase):
    def test_index(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('info' in response.context)


class RequestTest(TestCase):
    def test_requests(self):
        url = reverse('requests')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('request' in response.context)
