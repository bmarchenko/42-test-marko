# -*- coding: utf-8 -*-
from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField('Name', max_length=50, blank=True, null=True)
    surname = models.CharField('Last Name', max_length=50, blank=True, null=True)
    birthday = models.DateField('Date of birth', blank=True, null=True)
    bio = models.TextField('Bio', blank=True, null=True)
    email = models.EmailField('email', max_length=50, blank=True, null=True)
    jabber = models.CharField('Jabber', max_length=50, blank=True, null=True)
    skype = models.CharField('Skype', max_length=50, blank=True, null=True)
    other_contacts = models.TextField('Other contacts', blank=True, null=True)

    def __unicode__(self):
         return self.name
