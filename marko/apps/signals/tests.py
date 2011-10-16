from django.test import TestCase
from firstapp.models import PersonalInfo
from signals.models import SignalsSave
import datetime

class SignalTest(TestCase):
    
    def test_creation(self):
        info = PersonalInfo()
        info.name = 'Name'
        info.surname = 'Surname'
        info.birthday = '1988-01-23'
        info.bio = 'Info'
        info.save()
        
        signal = SignalsSave.objects.all().order_by('-time')[0]

        self.assertEquals(signal.signal_type, 'creation')
        self.assertEquals(signal.sender, 'PersonalInfo')


      
    def test_deletion(self):
        person = PersonalInfo.objects.get(id=1)
        person.delete()

        signal = SignalsSave.objects.all().order_by('-time')[0]
        self.assertEquals(signal.signal_type, 'deletion')
     #   self.assertEquals(unicode(log.model_class), unicode(person.__class__))
