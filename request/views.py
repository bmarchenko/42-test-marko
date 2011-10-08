# -*- coding: utf-8 -*-

from request.models import Request
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template

def request(request, template_name="request.html"):
    request = Request.objects.all()
    return render_to_response(template_name, {'request' : request})



