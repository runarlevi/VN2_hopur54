from django.shortcuts import render

products = [
    {'name': 'Fortnite', 'price': '99'},
    {'name': 'Call of Duty', 'price': '100'}
]
# Create your views here.
def index(request):
    return render(request, 'products/index.html', context={
        'products': products,
    })