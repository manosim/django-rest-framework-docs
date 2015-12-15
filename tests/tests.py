from django.test import TestCase


class SimpleTest(TestCase):

    def test_details(self):
        self.assertEqual(1, 1)
