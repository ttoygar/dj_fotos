from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from fotos.views import home


# Create your tests here.
class HomeTest(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'fotos/home.html')
