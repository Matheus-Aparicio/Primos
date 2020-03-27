from django.shortcuts import render
from .models import Historico

# Create your views here.


def index(request):
    numeros = Historico.objects.all().order_by('-id')
    return render(request, "historico/index.html", { 'numeros': numeros })
