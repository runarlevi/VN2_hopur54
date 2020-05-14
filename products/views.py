from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.forms.product_form import ProductCreateForm, ProductUpdateForm
from products.models import Product, ProductImage

from cart.models import ShoppingCart
from user.models import Profile, UserHistory


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(released=True).order_by('name')}
    return render(request, 'products/index.html', context)

# /products/{:id}
#@login_required
def get_product_by_id(request, id):
    history = UserHistory(product_id=id, user_id=request.user.id)
    history.save()
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('products-index')
    else:
        form = ProductCreateForm()
    return render(request, 'products/create_product.html', {
        'form': form
    })

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products-index')

@login_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'products/update_product.html', {
        'form': form,
        'id': id,
    })

@login_required
def add_to_cart(request, id):
    # ShoppingCart.objects.all().delete()
    if ShoppingCart.objects.filter(product_id=id, user_id=request.user.id).exists():
        print('in if')
        my_shopping_cart = ShoppingCart.objects.get(product_id=id, user_id=request.user.id)
        my_shopping_cart.quantity += 1
        my_shopping_cart.save(update_fields=['quantity'])
        messages.info(request, 'This item was added to your cart.')
    else:
        to_cart = ShoppingCart(product_id=id, user_id=request.user.id, quantity=1)
        to_cart.save()
        messages.info(request, 'This item was added to your cart.')

    return redirect('product_details', id=id)

def filter_consoles(request):
    my_context = {
        'consoles': Product.objects.filter(category=1),
    }
    return render(request, 'home/index.html', my_context)

def filter_games(request):
    my_context = {
        'games': Product.objects.filter(category=2),
    }
    return render(request, 'home/index.html', my_context)

def filter_accessories(request):
    my_context = {
        'accessories': Product.objects.filter(category=3),
    }
    return render(request, 'home/index.html', my_context)