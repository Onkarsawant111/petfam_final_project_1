from django.contrib import admin
from .models import Order, Order_items, Shipping_address, gpay_scanner, AmountPaidPicture

# Register your models here.
class ShippingAddress(admin.ModelAdmin):
    list_display = ['id','user','name','email','address','city','zipcode','state','country']
admin.site.register(Shipping_address, ShippingAddress)
class Orders(admin.ModelAdmin):
    list_display = ['id','name','email','address','amount_paid','date_ordered','shipped']
admin.site.register(Order, Orders)
class Ordered_items(admin.ModelAdmin):
    list_display = ['id','user','order','product','price']
admin.site.register(Order_items, Ordered_items)
class Gpay_scanner(admin.ModelAdmin):
    list_display = ['id','img']
admin.site.register(gpay_scanner, Gpay_scanner)

class Amountpaidpic(admin.ModelAdmin):
    list_display = ['payment_image']
admin.site.register(AmountPaidPicture, Amountpaidpic)


# making two models inline i.e. on same page in admin panel
#Order & Order_items model together
class Orderiteminline(admin.StackedInline):
    model = Order_items
    extra = 0

# extend our Order model
class Orderadmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'name', 'email', 'address', 'amount_paid', 'date_ordered', 'shipped', 'date_shipped']
    readonly_fields = ['date_ordered'] 
    inlines = [Orderiteminline]

#unregister Order model
admin.site.unregister(Order)

#re-register Order & Order_items
admin.site.register(Order, Orderadmin)







