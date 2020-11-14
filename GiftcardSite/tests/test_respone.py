from django.test import TestCase, Client
from django.urls import reverse
from LegacySite.models import *
from LegacySite.views import *
from django.http import HttpRequest


import json

class TestResponse(TestCase):
     def setUp(self):
          self.client = Client()


     def test_correct_autoescaping(self):
          prouct1 = Product.objects.create(product_name = 'test', product_image_path= 'test', recommended_price = 1, description = 'test')
          #section = Section.objects.create(name='<a>evil</a>')
          response = self.client.get('/buy',{'director' : '<a>evil</a>'})
          #print("I'm in test_response")
          #print(response.content)
          self.assertNotContains(response, "<a>evil</a>", status_code=200)
          self.assertContains(response, "&lt;a&gt;evil&lt;/a&gt;", status_code=200)

