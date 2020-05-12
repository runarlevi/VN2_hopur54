from django.forms import ModelForm, widgets
from django import forms

#from cart.models import ShoppingCart, CheckoutForm


class SomeForm(ModelForm):
    class Meta:
        #model = CheckoutForm
        exclude = ['id']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postcode': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class myCheckoutForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'John Johnson'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'John@Johnson.com'
    }))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St'
    }))
    #country = CountryField(blank_label='(Select country)')
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'New York'
    }))
    zip = forms.CharField()
