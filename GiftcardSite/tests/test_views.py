from django.test import TestCase, Client
from django.urls import reverse
from LegacySite.models import *
import json

class TestViews(TestCase):

     def setUp(self):
          self.client = Client()
          self.index_url = reverse('index')
          self.register_url = reverse('Register')
          self.register_url = reverse('Buy Gift Card')
          self.register_url = reverse('Gift a Card')
          self.register_url = reverse('Login')
          self.register_url = reverse('Logout')
          self.register_url = reverse('Use a card')


     def test_legacySite_index_GET(self):
          #client = Client()

          response = self.client.get(reverse('index'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'index.html')

     def test_legacySite_register_GET(self):
          #client = Client()
          response = self.client.get(reverse('Register'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'register.html')
"""
     def test_legacySite_BuyGiftCard_GET(self):
          #client = Client()
          response = self.client.get(reverse('Buy Gift Card'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'item-single.html')

     def test_legacySite_GiftaCard_GET(self):
          #client = Client()
          response = self.client.get(reverse('Gift a Card'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'gift.html')

     def test_legacySite_login_GET(self):
          #client = Client()
          response = self.client.get(reverse('Login'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'login.html')

     def test_legacySite_logout_GET(self):
          #client = Client()
          response = self.client.get(reverse('Logout'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'logout.html')

     def test_legacySite_useacard_GET(self):
          #client = Client()
          response = self.client.get(reverse('Use a card'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'use.html')


"""
