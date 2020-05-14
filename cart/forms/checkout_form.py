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

    cardholder = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'Enter your name',
    }))

    cardnumber = forms.CharField(max_length=16, min_length=16, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0000 0000 0000 0000',
    }))

    month = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '',
    }))

    year = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    cvc = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'cvv',
        'placeholder': '123'
    }))