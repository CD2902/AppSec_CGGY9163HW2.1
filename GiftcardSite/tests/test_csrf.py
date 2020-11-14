from django.test import TestCase, Client
from django.urls import reverse
from LegacySite.models import *
from LegacySite.views import *
from django.http import HttpRequest
from bs4 import BeautifulSoup



import json

class TestResponse(TestCase):
     def setUp(self):
          self.client = Client()

     def test_correct_autoescaping(self):
          prouct1 = Product.objects.create(product_name = 'test', product_image_path= 'test', recommended_price = 1, description = 'test')
          response = self.client.get(reverse('Gift a Card'))
          print(response)
          soup = BeautifulSoup(response.content)
          print(soup)
          testsoupfind = soup.find('input', {'name': 'csrfmiddlewaretoken'})
          print(response.content)
          print(testsoupfind)
