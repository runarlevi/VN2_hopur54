from django.db.models import Sum
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
    my_shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id)
    for item in my_shopping_cart:
        total += item.quantity * my_products.filter(id=item.product_id)[0].price # Þarf kannski að nota primary key?
    context = {
        'cart': my_shopping_cart,
        'total': "{:.2f}".format(total),
    }
    return render(request, 'cart/index.html', context)


def remove_from_cart(request):
    pass


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = myCheckoutForm()
        context = {
            'form': form,
        }
        return render(self.request, 'cart/checkout.html', context)

    def post(self, *args, **kwargs):
        form = myCheckoutForm(self.request.POST or None)
        if form.is_valid():
            print('The form is valid')
            return redirect('checkout')



'''
def do_checkout(request):
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
'''