from django.shortcuts import render, redirect
from .models import Shipping_address
from .forms import Shippingform
from cart.cart import Cart
from django.contrib import messages

def checkout(request):
    cart = Cart(request)
    total = cart.cart_total_price()
    cart_products = cart.get_prods()

    if request.user.is_authenticated:
        try:
            shipping_user = Shipping_address.objects.get(user=request.user)
            shipping_form = Shippingform(request.POST or None, instance=shipping_user)
        except Shipping_address.DoesNotExist:
            shipping_user = None
            shipping_form = Shippingform(request.POST or None)

        if request.method == 'POST':
            if shipping_form.is_valid():
                shipping_instance = shipping_form.save(commit=False)
                shipping_instance.user = request.user
                shipping_instance.save()
                return redirect('checkout_success')  # Replace with your desired URL name

        return render(request, 'checkout.html', {'cart_products': cart_products, 'total': total, 'shipping_form': shipping_form})
    else:
        return redirect('user_login')  # Redirect to login page if user is not authenticated

def billing_info(request):
    if request.POST: # when user use "POST" method after clicking button(Countinue to payment) in 'checkout.html' page
        cart = Cart(request)
        total = cart.cart_total_price()
        cart_products = cart.get_prods()
        shipping_info = request.POST
        request.session['my_shipping'] = shipping_info  #first we crated session i.e '[my_shipping]' we can use this session in another views functions


        return render(request, 'billing_info.html', {'cart_products': cart_products, 'total': total, 'shipping_info':shipping_info})
    else:
        messages.success(request, 'Access denied')  
        return redirect('home')
    
def process_order(request): # it is created to add shipping address to our model 'Shipping_address' in admin panel
    if request.POST: 
        my_shipping = request.session.get('my_shipping') # getting data from session created above
        print(my_shipping)
        messages.success(request, 'Order placed successfully, Thank you!')
        return redirect('home')


