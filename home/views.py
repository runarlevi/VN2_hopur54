from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from products.models import Product


def index(request):
    my_context = {
        'upcoming': Product.objects.filter(released=False),
    }
    return render(request, 'home/index.html', my_context)