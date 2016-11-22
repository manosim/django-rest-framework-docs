"""
Defining a custom template tag as a wrapper around the restructuredtext template tag provided by the
django-markwhat library. This prevents the need for users to also install django-markwhat into their
INSTALLED_APPS.
"""
from django import template
from django_markwhat.templatetags.markup import restructuredtext

register = template.Library()


@register.filter(is_safe=True)
def rst(value):
    return restructuredtext(value)
