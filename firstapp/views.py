# -*- coding: utf-8 -*-

from firstapp.models import PersonalInfo
from firstapp.forms import PersonalInfoForm
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def home(request, template_name="home.html"):
    info = get_object_or_404(PersonalInfo, id = 1)
    return render_to_response(template_name, {'info' : info}, context_instance=RequestContext(request))

@login_required
def edit(request, form_class=PersonalInfoForm, template_name="edit.html"):
    info = get_object_or_404(PersonalInfo, id = 1)
    info_form = form_class(instance = info)
    if request.method == "POST" and request.POST.get("action") == "update":
        info_form = form_class(request.POST, instance = info)
        if info_form.is_valid():
            info = info_form.save(commit=False)
            info.save()           
            return HttpResponseRedirect(reverse("home"))
        
                
    return render_to_response(template_name, {
        "info_form": info_form,
        "info":info,
        
    }, context_instance=RequestContext(request))
