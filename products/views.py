from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from products.forms.product_form import ProductCreateForm, ProductUpdateForm
from products.models import Product, ProductImage


# Create your views here.
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
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

# /products/{:id}
@login_required
def get_product_by_id(request, id):
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