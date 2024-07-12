from django.urls import path
from . import views

urlpatterns = [
    path('cart_summary', views.cart_summary, name='cart_summary'),
    path('cartadd', views.cartadd, name='cartadd'),
    path('cartdelete', views.cartdelete, name='cartdelete'),
    path('cartupdate', views.cartupdate, name='cartupdate'),
]
