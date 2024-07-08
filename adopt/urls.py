from django.urls import path
from . import views

urlpatterns = [
    path('adopt-dog', views.dog, name='adopt-dog'),
]