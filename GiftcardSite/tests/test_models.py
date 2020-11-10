from django.test import TestCase
from LegacySite.models import *



class TestModels(TestCase):

     def setUp(self):
          self.Card1 = Card.objects.create( data = "test", prod = 1, fp = "test", amount = 1000, user="test")
