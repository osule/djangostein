from django.test import TestCase

from django.db import connections

class HomeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        dbnames = cls._databases_names()

    def test_home(self):
        pass
