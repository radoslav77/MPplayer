from django import forms
from .models import *


class Add(forms.Form):
    class Meta:
        model = Song

        fields = ('title', 'artist', 'image', 'audio_file')
