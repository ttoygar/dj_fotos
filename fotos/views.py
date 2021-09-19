from django.shortcuts import render

from .models import Fotolar
from .forms import FotoForm


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
