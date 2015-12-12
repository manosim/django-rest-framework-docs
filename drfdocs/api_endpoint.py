from django.contrib.admindocs.views import simplify_regex


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
        self.pattern = pattern
        self.name = pattern.name
        self.path = self._get_path(parent_pattern)
        self.view_name = pattern.callback.__name__

    def _get_path(self, parent_pattern):
        if parent_pattern:
            parent_path = simplify_regex(parent_pattern.regex.pattern)[:-1]
            return "{0}{1}".format(parent_path, simplify_regex(self.pattern.regex.pattern))
        return simplify_regex(self.pattern.regex.pattern)
