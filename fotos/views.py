from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Fotolar
from .forms import FotoForm


# Create your views here.
# def home(request):
#     return render(request, 'fotos/home.html', {'form':FotoForm()})


def home(request):
    form = FotoForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        print("POST!!")
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        else:
            form = FotoForm()
    table_content = Fotolar.objects.order_by('-tarih')
    context = {
        'table_content': table_content,
        'form': form,
    }

    return render(request, 'fotos/home.html', context=context)


# def home(request):
#     table_content = Fotolar.objects.order_by('-tarih')
#     context = {
#         'table_content': table_content,
#     }
#     return render(request, 'fotos/home.html', context=context)
