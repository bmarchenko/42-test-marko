from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from firstapp.models import PersonalInfo
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import date
import subprocess
import sys
from django.core.management import call_command

class HomePageTest(TestCase):
    fixtures = ['initial_data.json']

    def test_index(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('info' in response.context)

    def test_content(self):
        self.info = PersonalInfo.objects.get(id=1)
        self.assertEqual(self.info.name, 'Bogdan')
        self.assertEqual(self.info.surname, 'Marchenko')
        self.assertEqual(self.info.email, "bogdan.marko@gmail.com")
        self.assertEqual(self.info.jabber, "bogdan.marko@jabber.org")
        self.assertEqual(self.info.skype, "bogdan_marchenko")


class ChangeInfoTest(TestCase):
    def test_change(self):
        c = Client()
        self.assertTrue(c.login(username='admin', password='admin'))
        c.post(reverse('edit'), {'name': 'Hello', 'surname': 'World',
            'birthday': '1981-01-22', 'bio': 'info', 'email':
            'bogdan-ne@mail.ru', 'jabber': 'jabber', 'skype':
            'bogdan_marchenko', 'other_contacts': 'lkdf'})

        info = PersonalInfo.objects.get(id=1)
        self.assertEqual(info.name, 'Hello')
        self.assertEqual(info.surname, 'World')

    def test_reversed(self):
        self.assertTrue(self.client.login(username="admin", password="admin"))
        # A response
        response = self.client.get(reverse('edit'))
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        # Check if fields was reversed
        self.failIf(response.content.index('id="id_name"') <
                    response.content.index('id="id_other_contacts"'))

class ContextProcessorTest(TestCase):

    def test_context_processor(self):
        response = self.client.get(reverse('home'))
        try:
            s = response.context['settings']
        except:
            s = False
        self.assertTrue(s)
        self.assertEqual(s, settings)


class TagTest(TestCase):

    def test_tag_link(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '/admin/firstapp/personalinfo/1/',
                count=1, status_code=200)


class CalendarWidgetTest(TestCase):

    def test_js(self):
        js = '<script type="text/javascript" src="/static/js/widget-calendar.js"></script>'
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(reverse('edit'))
        self.assertContains(response, js, count=1)


class CommandTest(TestCase):

    def testCommand(self):
        ferr = ""
        fout = ""
        p = subprocess.Popen('python manage.py allobjects',
                shell=True, #assuming test are handled in Unix
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        p.wait()
        fout = p.stdout.read()
        self.failIfEqual(fout, "")
