from django.template.base import Library

register = Library()



@register.simple_tag
def edit_link(object):
    return "/admin/" + object._meta.app_label + "/" \
        + object._meta.module_name + "/" + str(object.id) + "/"
