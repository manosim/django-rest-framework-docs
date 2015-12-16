from django.core.urlresolvers import reverse
from django.test import TestCase


class SimpleTest(TestCase):

    def test_details(self):
        self.assertEqual(1, 1)


class DRFDocsViewTests(TestCase):
    def setUp(self):
        super(DRFDocsViewTests, self).setUp()

    def test_index_view_with_no_questions(self):
        """
        Should load the drf focs view
        """
        response = self.client.get(reverse('drfdocs'))

        # print()
        # print()
        # print(response)
        # print(response["context"])
        # print(response.context)
        # print(dir(response))
        # print()
        # print()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["endpoints"], [])
        # self.assertContains(response, "No polls are available.")
        # self.assertQuerysetEqual(response.context['latest_question_list'], [])
