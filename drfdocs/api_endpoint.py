from django.contrib.admindocs.views import simplify_regex


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
        self.pattern = pattern
        self.url_parent_regex = simplify_regex(parent_pattern.regex.pattern)[:-1] if parent_pattern else None
        self.url_regex = ("{0}{1}".format(self.url_parent_regex, simplify_regex(pattern.regex.pattern))) if self.url_parent_regex else simplify_regex(pattern.regex.pattern)
        self.url_name = pattern.name
        self.regex = simplify_regex(pattern._regex)
        self.view_name = pattern.callback.__name__
