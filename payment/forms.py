from django import forms
from .models import Shipping_address

class Shippingform(forms.ModelForm):  # .ModelForm collects data in the model of database
    name = forms.CharField(max_length=250, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=250, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=250, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=20, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(max_length=20, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=20, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    country = forms.CharField(max_length=20, required='', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta: # posting this form input details in which model:
        model = Shipping_address
        fields = ['name','email','address','city','zipcode','state','country']
        exclude = ['user',] # exclude the user field from above model 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        