from django import forms
from .models import Shipping_address

class Shippingform(forms.ModelForm):
    name = forms.CharField(max_length=250, required='')
    email = forms.EmailField(max_length=250, required='')
    address = forms.CharField(max_length=250, required='')
    city = forms.CharField(max_length=20, required='')
    zipcode = forms.CharField(max_length=20, required='')
    state = forms.CharField(max_length=20, required='')  
    country = forms.CharField(max_length=20, required='')

    class Meta: # posting this form input details in which model:
        model = Shipping_address
        fields = ['name','email','address','city','zipcode','state','country']
        exclude = ['user',] # exclude the user field from above model 