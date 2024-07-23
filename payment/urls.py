from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('billing_process/', views.billing_process, name='billing_process'),
]