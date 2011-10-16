from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from firstapp.models import PersonalInfo
from django.core.urlresolvers import reverse
from django.conf import settings


class HomePageTest(TestCase):
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
