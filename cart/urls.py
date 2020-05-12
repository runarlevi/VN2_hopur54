from django.urls import path
from . import views
from .views import CheckoutView

urlpatterns = [
    path('', views.index, name="shopping-cart-index"),
    path('checkout/', CheckoutView.as_view(), name="checkout")
]