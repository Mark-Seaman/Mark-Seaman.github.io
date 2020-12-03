from django.test import TestCase

from .models import Superhero


class HeroTests(TestCase):
    
    def test_create(self):
        Superhero.objects.create(name='xxx', identity='yyy')
        self.assertEqual(len(Superhero.objects.all()), 1)
        self.assertEqual(Superhero.objects.get(pk=1).name, 'xxx')
        self.assertEqual(Superhero.objects.get(pk=1).identity, 'yyy')
        
    def test_update(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        x.name = 'Iron Man'
        x.save()
        y = Superhero.objects.get(pk=1)
        self.assertEqual(y.name, 'Iron Man')
        self.assertEqual(y.identity, 'Bruce Banner')
        
    def test_read(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        self.assertEqual(x.name, 'Hulk')
        self.assertEqual(x.identity, 'Bruce Banner')
        
    def test_image(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        x.image = 'Hulk.jpg'
        x.save()
        self.assertEqual(x.image, 'Hulk.jpg')
        
