from django.test import TestCase
from django.test import SimpleTestCase
from .models import Hero
from django.urls import reverse


class ViewTests(TestCase):

    def setUp(self):
        self.hero = Hero.objects.create(name='Iron Man', identity='Tony Stark')
    
    def test_page_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hero_exists(self):
        self.assertEqual(len(Hero.objects.all()), 1)
        
        
    def test_list_view(self):
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero_list.html')
        self.assertContains(response, '<li>', count=1)
    
    