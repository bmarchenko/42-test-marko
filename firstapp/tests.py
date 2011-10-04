"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class HomePageTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

