from django.db import models
from django.db.models.base import Model

# Create your models here.

'''
class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True, upload_to='')
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title
'''


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    image = models.FileField(upload_to='', blank=True)
    audio_file = models.FileField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title
