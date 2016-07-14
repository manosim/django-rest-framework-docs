"""
Defining a custom template tag as a wrapper around the markup template tag provided by the
django-markwhat library. This prevents the need for users to have to install django-markwhat into their
INSTALLED_APPS.
"""
from django import template
from django_markwhat.templatetags.markup import markdown as markdown_filter

register = template.Library()


@register.filter(is_safe=True)
def markdown(value, args=''):
    return markdown_filter(value, args)
