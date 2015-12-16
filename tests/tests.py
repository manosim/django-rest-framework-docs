from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings


class DRFDocsViewTests(TestCase):

    SETTINGS_HIDE_DOCS = {
        'HIDDEN': True  # Default: False
    }

    def setUp(self):
        super(DRFDocsViewTests, self).setUp()

    def test_index_view_with_endpoints(self):
        """
        Should load the drf focs view with all the endpoints.
        NOTE: Views that do **not** inherit from DRF's "APIView" are not included.
        """
        response = self.client.get(reverse('drfdocs'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["endpoints"]), 8)

        # Test the login view
        self.assertEqual(response.context["endpoints"][0].name_parent, "accounts")
        self.assertEqual(response.context["endpoints"][0].allowed_methods, ['POST', 'OPTIONS'])
        self.assertEqual(response.context["endpoints"][0].path, "/accounts/login/")
        self.assertEqual(len(response.context["endpoints"][0].fields), 2)
        self.assertEqual(response.context["endpoints"][0].fields[0]["type"], "CharField")
        self.assertTrue(response.context["endpoints"][0].fields[0]["required"])

    @override_settings(REST_FRAMEWORK_DOCS=SETTINGS_HIDE_DOCS)
    def test_index_view_docs_hidden(self):
        """
        Should prevent the docs from loading the "HIDDEN" is set
        to "False" in settings
        """
        response = self.client.get(reverse('drfdocs'))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.reason_phrase, "NOT FOUND")