from django.shortcuts import render
from cart.models import ShoppingCart


def index(request):
    context = {'cart': ShoppingCart.objects.all()}
    return render(request, 'cart/index.html', context)