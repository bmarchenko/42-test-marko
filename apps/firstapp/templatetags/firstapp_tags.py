from django import template
from firstapp.models import PersonalInfo
register = template.Library()


def edit_link(obj):

