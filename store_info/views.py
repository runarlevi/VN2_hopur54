from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store_info/index.html')

def help(request):
    return render(request, 'store_info/help.html')

def contact_us(request):
    return render(request, 'store_info/contact_us.html')