# -*- coding: utf-8 -*-

from firstapp.models import PersonalInfo
from firstapp.forms import PersonalInfoForm
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import simplejson


def home(request, template_name="home.html"):
    info = get_object_or_404(PersonalInfo, id=1)
    return render_to_response(template_name, {'info': info}, \
context_instance=RequestContext(request))


@login_required
def edit(request, form_class=PersonalInfoForm, template_name="edit.html"):
    info = get_object_or_404(PersonalInfo, id=1)
    info_form = form_class(instance=info)
    if request.method != "POST":
        form = form_class(instance=info)
        return render_to_response(template_name, {
        "info_form": info_form,
        "info": info,
    }, context_instance=RequestContext(request))


    resp_dict = {'bad': False}
    form = PersonalInfoForm(request.POST, instance=info)
    if form.is_valid():
        form.save()
        if request.is_ajax():
            return HttpResponse(json.dumps(resp_dict, ensure_ascii=False),
                                mimetype='application/json')
        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        if request.is_ajax():
            resp_dict['bad'] = True
            errs = {}
            for item_id, err_val in form.errors.items():
                errs[item_id] = unicode(err_val)
            resp_dict['errs'] = errs
            return HttpResponse(json.dumps(resp_dict, ensure_ascii=False),
                                mimetype='application/json')

        else:
            return render_to_response('edit.html',
                   {'info_form': form, "info": info}, context_instance=RequestContext(request))
