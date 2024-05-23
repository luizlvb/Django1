from django.urls import path
from recipe.views import home, sobre, contato1



urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato1),
]