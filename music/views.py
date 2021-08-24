from django.shortcuts import redirect, render
from django.core.paginator import Paginator


# Create your views here.
from .models import *
from .forms import NewSong


def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, 'music/index.html', context)


def add(request):
    if request.method == 'POST':
        form = NewSong(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()

            return render(request, 'music/index.html', {
                'msg': ' Song has been added to your Library '
            })

    return render(request, 'music/add.html', {
        'form': NewSong()
    })
