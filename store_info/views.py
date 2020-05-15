from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'store_info/index.html')

def help(request):
    return render(request, 'store_info/help.html')

def contact_us(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid()():
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'store_info/contact_us.html', {'form':form})
