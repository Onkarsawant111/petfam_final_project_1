from django.shortcuts import render, get_object_or_404
from .cart import Cart
from products.models import Products
from django.contrib import messages
# once product data sent from products page to cartadd page we can send response to confirm success thus add jsonresponse:
from django.http import JsonResponse 

# Create your views here.
def cart_summary(request):
    cart = Cart(request) 
    total = cart.cart_total_price() # total price of products in cart
    cart_products = cart.get_prods # call the function of 'cart.py' 
    return render(request, 'cart_summary.html', {'cart_products':cart_products, 'total': total})

def cartadd(request):
    # first confirm if user is login or not or is he superuser:
    if request.user.is_authenticated or request.user.is_superuser:    
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
            # response = JsonResponse({
            #     'product id': product.id,
            #     'product name': product.name})
            # return response

            # get cart quantity to add in cart logo in navbar, above code is commented as we dont require json ressponse of product id and name in console
            cart_quantity = cart.__len__()
            messages.success(request, "Hooray! 🎉 You've successfully added the product to your cart. Happy shopping!")
            response = JsonResponse({'qty': cart_quantity, 'product name': product.name})
            return response
    else:
        messages.warning(request, "You need to be logged in to add items in your cart.")
        return JsonResponse({'error': 'User not authenticated'}, status=403)


def cartdelete(request):
    cart = Cart(request)
    if request.POST.get('action') == "post":
        # getting data from ajax request present in 'main.html'
        product_id = int(request.POST.get('product_id'))
        # call function in Cart class
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        return response

# def cartupdate(request):
#     return render(request, 'cartupdate.hmtl')