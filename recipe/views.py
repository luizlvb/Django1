
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipe/pages/home.html')

def sobre(request):
    return HttpResponse('sobre')

def contato1(request):
    return HttpResponse('contato')

    