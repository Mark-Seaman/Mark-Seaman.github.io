from django.test import TestCase

from .models import Superhero

class CrudTests(TestCase):

    def test_num_heroes(self):
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 0)

