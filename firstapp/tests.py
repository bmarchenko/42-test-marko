"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class HomePageTest(TestCase):
    

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('info' in response.context)
        self.assertEqual([poll.pk for poll in response.context['info']], [1])

class RequestTest(TestCase):
    def test_requests(self):
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('request' in response.context)
        self.assertEqual([poll.pk for poll in response.context['request']], [1])
