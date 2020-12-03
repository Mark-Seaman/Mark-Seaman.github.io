from django.db import models
from django.urls import reverse


class Note(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})
