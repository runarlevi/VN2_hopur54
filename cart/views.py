from django.shortcuts import render, redirect

from cart.forms.checkout_form import CheckoutForms
from cart.models import ShoppingCart, CheckoutForm


def index(request, id):
    context = {'cart': ShoppingCart.objects.all()}
    return render(request, 'cart/index.html', context)


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-index')
    else:
        form = CheckoutForms()
    return render(request, 'cart/checkout.html', {
        'form': form
    })
