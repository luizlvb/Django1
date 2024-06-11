from django.urls import path
from recipe import views



urlpatterns = [

    path('', views.home, name='recipes-home'),
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
    path('category/cafedamanha/', views.category),

]