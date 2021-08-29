from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.utils.datastructures import MultiValueDict

# Create your views here.
from .models import *
from .forms import Add


def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, 'music/index.html', context)


def add(request):
    if request.method == 'POST':
        form = request.POST, request.FILES

        mus = []
        for key in form:

            mus.append(key)

        if not isinstance(mus, MultiValueDict):
            for value in mus:
                if isinstance(value, str):
                    mus[key] = [x.strip()
                                for x in value.rstrip(',').split(',') if x]
            data = MultiValueDict(mus[0])
            music = MultiValueDict(mus[1])

            add_song = Song(title=data['title'], artist=data['artist'],
                            image=music['image'], audio_file=music['file'])
            add_song.save()

        return redirect('index')

    return render(request, 'music/input.html', {
        'form': Add()
    })
