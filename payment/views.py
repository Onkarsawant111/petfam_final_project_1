from django.shortcuts import render
from .models import Order, Order_items
from cart.cart import Cart 

# Create your views here.
def checkout(request):
    cart = Cart(request) 
    total = cart.cart_total_price() # total price of products in cart
    cart_products = cart.get_prods # call the function of 'cart.py' 
    return render(request, 'checkout.html', {'cart_products':cart_products, 'total': total})