from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from fotos.views import home


# Create your tests here.
class HomeTest(TestCase):

    def test_root_resolves_home(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_is_page_correct(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn("<title>Fotos</title>", html)
        self.assertTrue(html.endswith('</html>'))
