from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .models import *


def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, 'music/index.html', context)


#form = Form(request.POST, request.FILES)


# <form action="" method="post" enctype="multipart/form-data">
