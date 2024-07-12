from django.shortcuts import render, get_object_or_404
from .cart import Cart
from products.models import Products
# once product data sent from products page to cartadd page we can send response to confirm success thus add jsonresponse:
from django.http import JsonResponse 

# Create your views here.
def cart_summary(request):
    return render(request, 'cart.html')

def cartadd(request):
    # first confirm if user is login or not or is he superuser:
    if request.user.is_authenticated and request.user.is_superuser:    
        # get the product id and create session if not exist
        cart = Cart(request)
        # now get the actual data of product of this id into the session from database
        if request.POST.get('action') == 'post': #post from ajax request
            product_id = int(request.POST.get('product_id')) 
            # get all the data once above product_id matches with product id of Product model  
            product = get_object_or_404(Products, id = product_id)
            # now add this product into session that we created above. For adding this product into session we need to create add function in 'cart.py'
            cart.add(product = product)
            # return response after succesful addition of product into session
            response = JsonResponse({
                'product id': product.id,
                'product name': product.name})
            return response

def cartdelete(request):
    return render(request, 'cartdelete.hmtl')

def cartupdate(request):
    return render(request, 'cartupdate.hmtl')