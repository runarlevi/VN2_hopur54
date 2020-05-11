from django.shortcuts import render
from products.models import Product


def index(request):
    my_context = {
        'upcoming': Product.objects.filter(released=False),
    }
    return render(request, 'home/index.html', my_context)