from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):  # complete order will be into this
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.TextField(max_length=250)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'
    
class Order_items(models.Model): # it contains all the cart items in it 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order-item - {str(self.id)}'