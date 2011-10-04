# -*- coding: utf-8 -*-
from firstapp.models import PersonalInfo

from django.contrib import admin
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

admin.site.register(PersonalInfo, PersonalInfoAdmin)

