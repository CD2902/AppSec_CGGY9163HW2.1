from django.test import TestCase, Client
from django.urls import reverse
from LegacySite.models import *
from LegacySite.views import *
from django.http import HttpRequest
#from bs4 import BeautifulSoup
import io


import json

class TestResponse(TestCase):
     def setUp(self):
          self.client = Client()


     def test_SQLi(self):
          password = 'test_pass_to_attack'
          User1 = User.objects.create(username='admin1', password='test_pass_to_attack')
          #self.client.login(username = 'admin', password = password)
          data = io.StringIO('{"merchant_id": "NYU Apparel Card", "customer_id": "chrisd", "total_value": "12313", "records": [{"record_type": "amount_change", "amount_added": 2000, "signature": " \' union SELECT password from LegacySite_user --"}]}')
          filename="newcard (3).gftcrd"
          response = self.client.post(reverse('Use a card'), {'card_data': data, 'filename' :filename, 'card_supplied': True, 'card_fname': 'test'},)
          #print(response.content)
          self.assertNotContains(response, password)









