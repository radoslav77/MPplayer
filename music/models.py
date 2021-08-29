from django.db import models
from django.db.models.base import Model

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    image = models.FileField(upload_to='', blank=True)
    audio_file = models.FileField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title
