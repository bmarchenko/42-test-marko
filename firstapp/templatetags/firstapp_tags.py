from django import template

from firstapp.models import PersonalInfo

register = template.Library()

def edit_link(obj):
  
    return obj.get_admin_url()



register.simple_tag(edit_link)
