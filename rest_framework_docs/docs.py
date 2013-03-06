import jsonpickle
import sys
import re
from django.conf import settings
from django.utils.importlib import import_module
from rest_framework.views import APIView
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from itertools import groupby


class DocumentationGenerator():
    """
    Creates documentation for a list of URL patterns pointing to
    Django REST Framework v.2.0, 2.1.3 APIView instances. The
    documentation is created by looking at the view's docstrings,
    the URL pattern objects, the view's serializers and other properties
    """

    def __init__(self, urlpatterns=None):
        """
        Sets urlpatterns
        urlpatterns -- List of UrlPatterns
        """
        if urlpatterns is None:
            urlpatterns = self.get_url_patterns()

        self.urlpatterns = urlpatterns

    def get_url_patterns(self):

        urls = import_module(settings.ROOT_URLCONF)
        patterns = urls.urlpatterns

        api_url_patterns = []
        patterns = self._flatten_patterns_tree(patterns)

        for pattern in patterns:
            for pattern in patterns:
                # If this is a CBV, check if it is an APIView
                if (hasattr(pattern.callback, 'cls_instance') and
                     issubclass(pattern.callback.cls_instance.__class__, APIView)):
                    api_url_patterns.append(pattern)

        # get only unique-named patterns, its, because rest_framework can add
        # additional patterns to distinguish format
        api_url_patterns = self._filter_unique_patterns(api_url_patterns)
        return api_url_patterns

    def _flatten_patterns_tree(self, patterns):
        """
        Uses recursion to flatten url tree

        patterns - urlpatterns list
        """
        pattern_list = []
        for pattern in patterns:
            if isinstance(pattern, RegexURLPattern):
                pattern_list.append(pattern)
            elif isinstance(pattern, RegexURLResolver):
                pattern_list.extend(self._flatten_patterns_tree(pattern.url_patterns))
        return pattern_list

    def _filter_unique_patterns(self, patterns):
        """
        Gets only unique patterns by its names
        """
        unique_patterns = []
        # group patterns by its names
        grouped_patterns = groupby(patterns, lambda pattern: pattern.name)
        for name, group in grouped_patterns:
            group_list = list(group)
            # choose from group pattern with shortest regex
            unique = min(group_list, key=lambda pattern: len(pattern.regex.pattern))
            unique_patterns.append(unique)

        return unique_patterns

    def get_docs(self, as_objects=False):
        """
        Gets the documentation as a list of objects or a JSON string

        as_objects -- (bool) default=False. Set to true to return objects instead of JSON
        """
        docs = self.__process_urlpatterns()
        docs.sort(key=lambda x: x.path)  # Sort by path

        if as_objects:
            return docs
        else:
            return jsonpickle.encode(docs, unpicklable=False)

    def __process_urlpatterns(self):
        """ Assembles ApiDocObject """
        docs = []

        for endpoint in self.urlpatterns:

            # Skip if URL isn't bound to a view
            if not endpoint.callback:
                continue

            # Build object and add it to the list
            doc = self.ApiDocObject()
            doc.title = self.__get_title__(endpoint)
            parsed_docstring = self.__parse_docstring__(endpoint)
            doc.description = parsed_docstring['description']
            doc.params = parsed_docstring['params']
            doc.path = self.__get_path__(endpoint)
            doc.model = self.__get_model__(endpoint)
            doc.allowed_methods = self.__get_allowed_methods__(endpoint)
            doc.fields = self.__get_serializer_fields__(endpoint)
            docs.append(doc)
            del(doc)  # Clean up

        return docs

    def __get_title__(self, endpoint):
        """
        Gets the URL Pattern name and make it the title
        """
        try:
                name = endpoint.name
                title = re.sub('[-_]', ' ', name)
                return title.title()
        except:
            return None

    def __parse_docstring__(self, endpoint):
        """
        Parses the view's docstring and creates a description
        and a list of parameters
        Example of a parameter:

            myVar -- a variable
        """

        try:  # Get API Doc String
            docstring = endpoint.callback.__doc__
            description = self.__trim(docstring)
            split_lines = description.split('\n')
            trimmed = False  # Flag if string needs to be trimmed
            _params = []

            for line in split_lines:
                if not trimmed:
                    needle = line.find('--')
                    if needle != -1:
                        trim_at = description.find(line)
                        description = description[:trim_at]
                        trimmed = True

                params = line.split(' -- ')
                if len(params) == 2:
                    _params.append([params[0].strip(), params[1].strip()])

            return {'description': description, 'params': _params}
        except:
            return None

    def __get_path__(self, endpoint):
        """
        Gets the endpoint path based on the regular expression
        pattern of the URL pattern. Cleans out the regex characters
        and replaces with RESTful URL descriptors
        """
        try:  # Get the URL
            cleaned = endpoint.regex.pattern
            cleaned = re.sub('\([^<]*<', '{', cleaned)
            cleaned = re.sub('>[^\)]*\)', '_id}', cleaned)
            cleaned = re.sub('^\^|/\??\$$', '', cleaned)
            cleaned = re.sub('\$$', '', cleaned)
            return cleaned
        except:
            return None

    def __get_model__(self, endpoint):
        """
        Gets associated model from the view
        """
        try:
            return endpoint.callback.cls_instance.model.__name__
        except:
            return None

    def __get_allowed_methods__(self, endpoint):
        """
        Gets allowed methods for the API. (ie. POST, PUT, GET)
        """
        try:  # Get the allowed methods
            return endpoint.callback.cls_instance.allowed_methods
        except:
            pass

    def __get_serializer_fields__(self, endpoint):
        """
        Gets serializer fields if set in the view. Returns dictionaries
        with field properties (read-only, default, min and max length)
        """
        try:  # Get the model's serializer fields
            serializer = endpoint.callback.cls_instance.get_serializer_class()

            fields = serializer().get_fields()

            data = []

            for name, field in fields.items():

                field_data = {}
                CAMELCASE_BOUNDARY = '(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))'
                field_name = re.sub(CAMELCASE_BOUNDARY, ' \\1', field.__class__.__name__)
                field_data['type'] = field_name
                try:
                    field_data['read_only'] = field.read_only
                except:
                    pass
                try:
                    field_data['default'] = field.default
                except:
                    pass
                try:
                    field_data['max_length'] = field.max_length
                except:
                    pass
                try:
                    field_data['min_length'] = field.min_length
                except:
                    pass
                data.append({name: field_data})

            return data
        except:
            return None

    def __trim(self, docstring):
        """
        Trims whitespace from the docstring in accordance to the PEP-257 standard
        From: http://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
        """
        if not docstring:
            return ''
        # Convert tabs to spaces (following the normal Python rules)
        # and split into a list of lines:
        lines = docstring.expandtabs().splitlines()
        # Determine minimum indentation (first line doesn't count):
        indent = sys.maxint
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))
        # Remove indentation (first line is special):
        trimmed = [lines[0].strip()]
        if indent < sys.maxint:
            for line in lines[1:]:
                trimmed.append(line[indent:].rstrip())
        # Strip off trailing and leading blank lines:
        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)
        # Return a single string:
        return '\n'.join(trimmed)

    class ApiDocObject(object):
        """ API Documentation Object """
        path = None
        title = None
        description = None
        params = []
        allowed_methods = []
        model = None
