# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from webblog.views import cover


class HomePageTest(TestCase):

    def test_root_url_resolves_to_cover_view(self):
        found = resolve('/webblog/')
        self.assertEqual(found.func, cover)
