# -*- coding: utf-8 -*-

from django import forms
from firstapp.models import PersonalInfo
import json

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo

   