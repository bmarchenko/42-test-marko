# -*- coding: utf-8 -*-
from django import forms
from firstapp.models import PersonalInfo
from firstapp.widgets import JQCalendarWidget

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        widgets = {'birthday': JQCalendarWidget}
