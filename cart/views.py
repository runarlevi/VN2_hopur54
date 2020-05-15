from django.contrib import messages
from django.db.models import Sum
from django.http import request
from django.shortcuts import render, redirect

#from cart.forms.checkout_form import CheckoutForms
from django.views import View

from cart.forms.checkout_form import myCheckoutForm
from cart.models import ShoppingCart
from products.models import Product
from user.models import Profile


def index(request):
    total = 0
    my_products = Product.objects
    my_shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id).order_by('product__name')
    for item in my_shopping_cart:
        total += item.quantity * my_products.filter(id=item.product_id)[0].price # Þarf kannski að nota primary key?
    context = {
        'cart': my_shopping_cart,
        'total': "{:.2f}".format(total),
    }
    return render(request, 'cart/index.html', context)


def decrease_quantity(request, id):
    my_shopping_cart = ShoppingCart.objects.get(product_id=id, user_id=request.user.id)
    if my_shopping_cart.quantity == 1:
        my_shopping_cart.delete()
        messages.info(request, 'Item quantity was decreased.')
        return redirect('shopping-cart-index')
    my_shopping_cart.quantity -= 1
    my_shopping_cart.save(update_fields=['quantity'])
    messages.info(request, 'Item quantity was decreased.')
    return redirect('shopping-cart-index')

def increase_quantity(request, id):
    my_shopping_cart = ShoppingCart.objects.get(product_id=id, user_id=request.user.id)
    my_shopping_cart.quantity += 1
    my_shopping_cart.save(update_fields=['quantity'])
    messages.info(request, 'Item was increased.')

    return redirect('shopping-cart-index')

def delete_row(request, id):
    my_shopping_cart = ShoppingCart.objects.get(product_id=id, user_id=request.user.id)
    my_shopping_cart.delete()
    messages.info(request, 'Item was deleted from your cart.')
    return redirect('shopping-cart-index')

def checkout_view(request):
    if request.method == 'POST':
        total = 0
        my_products = Product.objects
        my_shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id).order_by('product__name')
        for item in my_shopping_cart:
            total += item.quantity * my_products.filter(id=item.product_id)[0].price  # Þarf kannski að nota primary key?
        form = myCheckoutForm(data=request.POST)
        if form.is_valid():
            context = {
                'cart': my_shopping_cart,
                'total': "{:.2f}".format(total),
                'data': form.cleaned_data
            }
            return render(request, 'cart/payment.html', context)
        messages.warning(request, "Failed checkout")
        return redirect('checkout')
    else:
        form = myCheckoutForm()
    return render(request, 'cart/checkout.html', {
        'form': form
    })

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = myCheckoutForm()
        context = {
            'form': form,
        }
        return render(self.request, 'cart/checkout.html', context)

    def post(self, *args, **kwargs):
        total = 0
        my_products = Product.objects
        my_shopping_cart = ShoppingCart.objects.filter(user_id=self.request.user.id).order_by('product__name')
        for item in my_shopping_cart:
            total += item.quantity * my_products.filter(id=item.product_id)[
                0].price  # Þarf kannski að nota primary key?
        context = {
            'cart': my_shopping_cart,
            'total': "{:.2f}".format(total),
        }
        form = myCheckoutForm(self.request.POST or None)
        if form.is_valid():
            print('The form is valid')
            context['data'] = form.cleaned_data
            return render(self.request, 'cart/payment.html', context)
        messages.warning(self.request, "Failed checkout")
        return redirect('checkout')

def payment(request):
    total = 0
    my_products = Product.objects
    my_shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id).order_by('product__name')
    for item in my_shopping_cart:
        total += item.quantity * my_products.filter(id=item.product_id)[0].price
    context = {
        'cart': my_shopping_cart,
        'total': "{:.2f}".format(total),
    }
    return render(request, 'cart/payment.html', context)

def confirmation(request):
    my_shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id)
    for item in my_shopping_cart:
        all_prods = Product.objects.get(pk=item.product_id)
        all_prods.stock -= 1
        all_prods.save(update_fields=['stock'])
        item.delete()
    return render(request, 'cart/confirmation.html')
