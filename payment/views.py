from django.shortcuts import render, redirect
from .models import Shipping_address
from .forms import Shippingform
from cart.cart import Cart
from django.contrib import messages
from payment.models import Order, Order_items
from django.contrib.auth.models import User
from products.models import Products

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
        cart = Cart(request)
        total = cart.cart_total_price()
        cart_products = cart.get_prods()

        my_shipping = request.session.get('my_shipping') # getting data from above created session 

        # gather shipping info to push it in our 'Order' model
        name = my_shipping['name']
        email = my_shipping['email']
        #create shipping address from above session
        shipping_address = f"{my_shipping['name']}\n{my_shipping['email']}\n{my_shipping['address']}\n{my_shipping['city']}\n{my_shipping['zipcode']}\n{my_shipping['state']}\n{my_shipping['country']}"
        amount_paid = total  # to pass it in our 'Order' model

        #create an order in 'Order' model
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user, name=name, email=email, address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            # Now add order items in our 'Order_items' model
            order_id = create_order.pk # it gets the primary key(id) of the 'Order' model
            # get the info of products inside above Order 
            for product in cart_products:  # form above Cart 
                #get product id
                product_id = product.id
                #get product price
                price = product.price
                create_order_item = Order_items(user=user, order_id=order_id, product_id=product_id, price=price)
                create_order_item.save()

            messages.success(request, 'Order placed successfully, Thank you!')
            return redirect('home')


