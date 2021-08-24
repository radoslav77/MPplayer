from django import forms
from django.db.models import fields
from .models import *


class NewSong(forms.Form):
    class Meta:
        model = Song

        fields = ('title', 'artist', 'image', 'audio_file', 'duration')
