from django.test import SimpleTestCase
from django.urls import reverse, resolve
from LegacySite.views import *
#from LegacySite.views import index, register_view , login_view, logout_view,  buy_card_view, gift_card_view, use_card_view 
# Create your tests here.


class TestUrls(SimpleTestCase):

     def test_indexurl_is_resolved(self):
          url=reverse('index')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, index)

     def test_buy_url_is_resolved(self):
          url=reverse('Buy Gift Card')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, buy_card_view)

     def test_gift_url_is_resolved(self):
          url=reverse('Gift a Card')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, gift_card_view)

     def test_login_url_is_resolved(self):
          url=reverse('Login')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, login_view)

     def test_register_url_is_resolved(self):
          url=reverse('Register')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, register_view)

     def test_logout_url_is_resolved(self):
          url=reverse('Logout')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, logout_view)

     def test_use_url_is_resolved(self):
          url=reverse('Use a card')
          #print(resolve(url))
          self.assertEquals(resolve(url).func, use_card_view)
