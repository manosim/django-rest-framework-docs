from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings
from rest_framework_docs.settings import DRFSettings


class DRFDocsViewTests(TestCase):

    SETTINGS_HIDE_DOCS = {
        'HIDE_DOCS': True,  # Default: False
        'LOGIN_REQUIRED': False,  # Default: False
    }

    def setUp(self):
        super(DRFDocsViewTests, self).setUp()

    def test_settings_module(self):

        settings = DRFSettings()

        self.assertEqual(settings.get_setting("HIDE_DOCS"), False)
        self.assertEqual(settings.get_setting("TEST"), None)

    def test_index_view_with_endpoints(self):
        """
        Should load the drf focs view with all the endpoints.
        NOTE: Views that do **not** inherit from DRF's "APIView" are not included.
        """
        response = self.client.get(reverse('drfdocs'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 16)

        # Test the login view
        endpoint = response.context["endpoints"][4]
        self.assertEqual(endpoint.name_parent, "accounts")
        self.assertEqual(endpoint.allowed_methods, ['POST', 'OPTIONS'])
        self.assertEqual(endpoint.path, "/accounts/login/")
        self.assertEqual(endpoint.docstring, "A view that allows users to login providing their username and password.")
        self.assertEqual(len(endpoint.fields), 2)
        self.assertEqual(endpoint.fields[0]["type"], "CharField")
        self.assertTrue(endpoint.fields[0]["required"])

        # The view "OrganisationErroredView" (organisations/(?P<slug>[\w-]+)/errored/) should contain an error.
        endpoint = response.context["endpoints"][12]
        self.assertEqual(str(endpoint.errors), "'test_value'")

    def test_index_search_with_endpoints(self):
        response = self.client.get("%s?search=reset-password" % reverse("drfdocs"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 2)
        self.assertEqual(response.context["endpoints"][1].path, "/accounts/reset-password/confirm/")
        self.assertEqual(len(response.context["endpoints"][1].fields), 3)

    @override_settings(REST_FRAMEWORK_DOCS=SETTINGS_HIDE_DOCS)
    def test_index_view_docs_hidden(self):
        """
        Should prevent the docs from loading the "HIDE_DOCS" is set
        to "True" or undefined under settings
        """
        response = self.client.get(reverse('drfdocs'))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.reason_phrase.upper(), "NOT FOUND")

    def test_index_view_with_existent_namespace(self):
        """
        Should load the drf docs view with all the endpoints contained in the specified namespace.
        NOTE: Views that do **not** inherit from DRF's "APIView" are not included.
        """
        # Test 'accounts' namespace
        response = self.client.get(reverse('drfdocs-filter', args=['accounts']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 6)

        # Test the login view
        self.assertEqual(response.context["endpoints"][0].name_parent, "accounts")
        self.assertEqual(response.context["endpoints"][0].allowed_methods, ['POST', 'OPTIONS'])
        self.assertEqual(response.context["endpoints"][0].path, "/accounts/login/")

        # Test 'organisations' namespace
        response = self.client.get(reverse('drfdocs-filter', args=['organisations']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 5)

        # The view "OrganisationErroredView" (organisations/(?P<slug>[\w-]+)/errored/) should contain an error.
        self.assertEqual(str(response.context["endpoints"][1].errors), "'test_value'")

        # Test 'members' namespace
        response = self.client.get(reverse('drfdocs-filter', args=['members']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 1)

    def test_index_search_with_existent_namespace(self):
        response = self.client.get("%s?search=reset-password" % reverse('drfdocs-filter', args=['accounts']))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 2)
        self.assertEqual(response.context["endpoints"][1].path, "/accounts/reset-password/confirm/")
        self.assertEqual(len(response.context["endpoints"][1].fields), 3)

    def test_index_view_with_existent_app_name(self):
        """
        Should load the drf docs view with all the endpoints contained in the specified app_name.
        NOTE: Views that do **not** inherit from DRF's "APIView" are not included.
        """
        # Test 'organisations_app' app_name
        response = self.client.get(reverse('drfdocs-filter', args=['organisations_app']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 6)
        parents_name = [e.name_parent for e in response.context["endpoints"]]
        self.assertEquals(parents_name.count('organisations'), 5)
        self.assertEquals(parents_name.count('members'), 1)

    def test_index_search_with_existent_app_name(self):
        response = self.client.get("%s?search=create" % reverse('drfdocs-filter', args=['organisations_app']))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 1)
        self.assertEqual(response.context["endpoints"][0].path, "/organisations/create/")
        self.assertEqual(len(response.context["endpoints"][0].fields), 3)

    def test_index_view_with_non_existent_namespace_or_app_name(self):
        """
        Should load the drf docs view with no endpoint.
        """
        response = self.client.get(reverse('drfdocs-filter', args=['non-existent-ns-or-app-name']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 0)

    def test_model_viewset(self):
        response = self.client.get(reverse('drfdocs'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["endpoints"][1].path, '/organisation-model-viewsets/')
        self.assertEqual(response.context["endpoints"][2].path, '/organisation-model-viewsets/<pk>/')
        self.assertEqual(response.context["endpoints"][1].allowed_methods, ['GET', 'POST', 'OPTIONS'])
        self.assertEqual(response.context["endpoints"][2].allowed_methods, ['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
        self.assertEqual(response.context["endpoints"][4].allowed_methods, ['POST', 'OPTIONS'])
        self.assertEqual(response.context["endpoints"][3].docstring, 'This is a test.')
