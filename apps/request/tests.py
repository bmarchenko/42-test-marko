from django.test import TestCase, Client
from django.conf import settings
from request.models import Request
from django.core.urlresolvers import reverse


class MiddlewareTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_requests(self):
        url = reverse('requests')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('request' in response.context)

    def test_middleware(self):
        self.client.get(reverse('home'))
        request = Request.objects.all().order_by('-time')[0]
        self.assertEqual(request.path, reverse('home'))
        self.assertEqual(request.method, 'GET')
