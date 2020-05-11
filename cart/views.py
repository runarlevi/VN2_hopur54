from django.shortcuts import render, redirect

from cart.forms.checkout_form import CheckoutForms
from cart.models import ShoppingCart
from user.models import Profile


def index(request, id):
    user_id = Profile.objects.get(user_id=request.user.id).id
    context = {'cart': ShoppingCart.objects.filter(user_id=user_id)}
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
        'form': form,
        'cart': ShoppingCart.objects.all(),
    })
