from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'store_info/index.html')

def help(request):
    return render(request, 'store_info/help.html')

def contact_us(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'store_info/contact_us.html', {'form':form})
