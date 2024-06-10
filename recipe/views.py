
from __future__ import absolute_import
from django.http import HttpResponse
from django.shortcuts import render
from recipe.factory import make_recipe

# Create your views here.

def home(request):
    return render(request, 'recipe/pages/home.html', context={
        'recipes': [ make_recipe() for _ in range(10) ],
    })

def recipe(request):
    return render(request, 'recipe/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })






