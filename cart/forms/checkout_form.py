from django import forms


class myCheckoutForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'John Johnson',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'you@example.com',
    }))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234 Main St'
    }))

    country = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'USA'
    }))

    state = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'New York'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'zip'
    }))
