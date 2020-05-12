from django.db.models import Sum
from django.shortcuts import render, redirect

#from cart.forms.checkout_form import CheckoutForms
from django.views import View

from cart.forms.checkout_form import myCheckoutForm
from cart.models import ShoppingCart
from user.models import Profile


def index(request):
    print(request.user.id)
    #user_id = Profile.objects.get(user_id=request.user.id).id
    '''
    shopping_cart = ShoppingCart.objects
    context = {
        'cart': shopping_cart.filter(user_id=user_id),
        'total': shopping_cart.filter(user_id=user_id).aggregate(Sum('price'))['price__sum'],
    }
    return render(request, 'cart/index.html', context)
    '''
    return render(request, 'cart/index.html')


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