from django.urls import path
from . import views

urlpatterns = [
    path('dog_products', views.dog_products, name='dog_products'),
    path('cat_products', views.cat_products, name='cat_products'),
    path('bird_products', views.bird_products, name='bird_products'),
    path('smallpet_products', views.smallpet_products, name='smallpet_products'),
]
