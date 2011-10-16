from django.db import models
from django.db.models import signals 
from django.dispatch import receiver

#from firstapp.models import PersonalInfo

class SignalsSave(models.Model):
    signal_type = models.CharField('signal_type', max_length=50, blank=True, null=True)
    sender = models.CharField('sender', max_length=50, blank=True, null=True)    
    time = models.DateTimeField(auto_now_add=True)
@receiver(signals.post_delete)

def my_callback(sender, **kwargs):
    s = SignalsSave.objects.create(sender=sender.__name__, signal_type='deletion')
    s.save()

@receiver(signals.post_save)

def my_callback1(sender, **kwargs):
    if sender != SignalsSave:
        if 'created' in kwargs:
                if kwargs['created']:
                    s = SignalsSave.objects.create(sender=sender.__name__, signal_type='creation')
                    s.save()
        else:
            s = SignalsSave.objects.create(sender=sender.__name__, signal_type='edition')
            s.save()
