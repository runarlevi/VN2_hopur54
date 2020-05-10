from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from products.models import Product


def index(request):
    # Þarf að hafa database-inn og Product modelið eins svo 'Released = False' virki.
    my_context = {
        'upcoming': Product.objects.all(),
    }
    return render(request, 'home/index.html', my_context)