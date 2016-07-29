from django import template
from django.template.defaultfilters import stringfilter
from rest_framework.utils.formatting import markup_description


register = template.Library()


@register.filter(name='markdown')
@stringfilter
def markdown(value):
    return markup_description(value)
