# -*- coding: utf-8 -*-
from django import forms
from firstapp.models import PersonalInfo
from firstapp.widgets import JSDataPickerWidget

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
       
    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget = JSDataPickerWidget()
