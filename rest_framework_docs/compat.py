try:
    from django.urls import (
        URLPattern,
        URLResolver,
    )
except ImportError:
    # Will be removed in Django 2.0
    from django.urls import (
        RegexURLPattern as URLPattern,
        RegexURLResolver as URLResolver,
    )


# This is from the similarly named compat.py file of django-rest-framework 3.7
def get_regex_pattern(urlpattern):
    """
    Get the raw regex out of the urlpattern's RegexPattern or RoutePattern.
    This is always a regular expression, unlike get_original_route above.
    """
    if hasattr(urlpattern, 'pattern'):
        # Django 2.0
        return urlpattern.pattern.regex.pattern
    else:
        # Django < 2.0
        return urlpattern.regex.pattern


def is_url_resolver(instance):
    return isinstance(instance, URLResolver)


def is_url_pattern(instance):
    return isinstance(instance, URLPattern)
