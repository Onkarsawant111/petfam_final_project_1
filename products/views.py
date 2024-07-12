from django.shortcuts import render
from .models import Products, Categories

# Create your views here.
def dog_products(request):
    dog_products = Products.objects.filter(category__name='dog_products')
    return render(request, 'products.html', {'dog_products': dog_products})

def cat_products(request):
    cat_products = Products.objects.filter(category__name='cat_products')
    return render(request, 'products.html', {'cat_products': cat_products})

def bird_products(request):
    bird_products = Products.objects.filter(category__name='bird_products')
    return render(request, 'products.html', {'bird_products': bird_products})

def smallpet_products(request):
    smallpet_products = Products.objects.filter(category__name='smallpet_products')
    return render(request, 'products.html', {'smallpet_products': smallpet_products})