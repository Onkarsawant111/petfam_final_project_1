from django.contrib import admin
from .models import Order, Order_items, Shipping_address

# Register your models here.
class ShippingAddress(admin.ModelAdmin):
    list_display = ['id','user','name','email','address','city','zipcode','state','country']
admin.site.register(Shipping_address, ShippingAddress)

class Orders(admin.ModelAdmin):
    list_display = ['id','name','email','address','amount_paid','date_ordered']
admin.site.register(Order, Orders)

class Ordered_items(admin.ModelAdmin):
    list_display = ['id','user','order','product','price']
admin.site.register(Order_items, Ordered_items)








