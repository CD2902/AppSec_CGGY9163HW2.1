from django.test import TestCase, Client
from django.urls import reverse
from LegacySite.models import *
from LegacySite.views import *
from django.http import HttpRequest


import json

class TestResponse(TestCase):
     def setUp(self):
          self.client = Client()


     def test_https(self):
          response = self.client.get('https://localhost:8000')
          assert(response.status_code == 200)

