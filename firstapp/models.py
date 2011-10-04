# -*- coding: utf-8 -*-
from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(u"Ім'я", max_length=50)
    surname = models.CharField(u'Прізвище', max_length=50)
    birthday = models.DateField()
    bio = models.TextField(u'Біографія')
    email = models.EmailField('email', max_length=50)
    jabber = models.CharField('Jabber', max_length=50)
    skype = models.CharField('Skype', max_length=50)
    other_contacts = models.TextField(u'Інші контакти')
