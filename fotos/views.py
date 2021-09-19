from django.shortcuts import render
from django.http import HttpResponse

from .models import Fotolar


# Create your views here.
def home(request):
    return render(request, "fotos/home.html")
