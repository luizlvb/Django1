from django.urls import path
from recipe import views



urlpatterns = [

    path('', views.home),
    path('recipes/', views.recipe),

]