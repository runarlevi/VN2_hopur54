from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="shopping-cart-index"),
    path('checkout', views.checkout, name="checkout")
]