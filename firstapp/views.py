# -*- coding: utf-8 -*-

from firstapp.models import PersonalInfo
from django.shortcuts import render_to_response



def home(request, template_name="home.html"):
    data = PersonalInfo.objects.all()
    return render_to_response(template_name, {'data' : data})
  

