from django.forms import ModelForm, widgets
from django import forms


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
