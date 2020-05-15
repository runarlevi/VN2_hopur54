from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/storeinfo
    path('', views.index, name="store-info-index"),
    path('help/', views.help, name="help"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('contact_confirmation/', views.contact_confirmation, name="contact_confirmation"),

]