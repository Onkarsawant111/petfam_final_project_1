from django.urls import path
from . import views

urlpatterns = [
    path('adopt-dog', views.dog, name='adopt-dog'),
    path('adopt-cat', views.cat, name='adopt-cat'),
    path('adopt-bird', views.bird, name='adopt-bird'),
    path('adopt-smallpet', views.smallpet, name='adopt-smallpet'),
]