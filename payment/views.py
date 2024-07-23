from django.shortcuts import render, redirect
from .models import Shipping_address
from .forms import Shippingform
from cart.cart import Cart

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
        return redirect('login')  # Redirect to login page if user is not authenticated

def billing_process(request):
    pass