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
          Card1 = Card.objects.create( data = """{"merchant_id": "NYU Apparel Card", "customer_id": "chrisd", "total_value": "1000", "records": [{"record_type": "amount_change", "amount_added": 2000, "signature": "[ insert crypto signature here ]"}]}""", prod = 1, fp = "test", amount = 1000, user="chrisd")
          response = self.client.post(reverse('Use a card'))
          print(response)
          soup = BeautifulSoup(response.content)
          print(soup)
          testsoupfind = soup.find('input', {'admin'})
          print(response.content)
          print(testsoupfind)










