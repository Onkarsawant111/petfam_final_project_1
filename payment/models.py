from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime

# Create your models here.
# very imp model as it gives us idea about which user has put the order in 'Order' model and also let us know that where we need to ship the order
class Shipping_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(max_length=20)  
    country = models.CharField(max_length=20)

    class Meta: #dont pluralize shipping_address
        verbose_name_plural = "shipping address"

    def __str__(self):
        return f'shipping address - {str(self.id)}'
class Order(models.Model):  # complete order will be into this
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.TextField(max_length=250)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order - {str(self.id)}'
    
# automatically add shipping date in 'date_shipped' above
@receiver(pre_save, sender=Order)
def set_shipped_date_on_update(sender, instance, **kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shipped = now


class Order_items(models.Model): # it contains all the cart items in it 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order-item - {str(self.id)}'