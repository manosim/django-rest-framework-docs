

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
