from django.test import TestCase


class HomePageTest(TestCase):

    def test_root_url_resolves_to_cover_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'webblog/cover.html')
