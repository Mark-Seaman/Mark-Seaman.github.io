from django.db import models
from django.urls import reverse


class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.identity

    def get_absolute_url(self): 
        return reverse('hero_detail', args=[str(self.id)])
