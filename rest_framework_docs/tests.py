from django_nose import FastFixtureTestCase
from django.conf.urls import url
from rest_framework_docs.docs import DocumentationGenerator


class DocsTests(FastFixtureTestCase):

    def test_urls(self):
        obj = DocumentationGenerator()
        obj.get_url_patterns()

    def test_get_title(self):
        """
        Tests formatting of title string:
         - Removes dashes and underscores
         - Puts in title case
        """
        endpoint = url(r'^/?$', 'url', name='my_api-documentation')
        obj = DocumentationGenerator()
        result = obj.__get_title__(endpoint)
        self.assertEquals('My Api Documentation', result)

    def test_parse_docstring(self):
        docstring = """
        This is my description

        myvar1 -- a beautiful var
        """
        obj = DocumentationGenerator()
        docstring_meta = obj.__parse_docstring__(docstring)

        self.assertEquals([['myvar1', 'a beautiful var']],
                          docstring_meta['params'])
        self.assertEquals('This is my description\n\n',
                          docstring_meta['description'])

