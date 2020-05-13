from django.urls import path
from . import views
from .views import CheckoutView

urlpatterns = [
    path('', views.index, name="shopping-cart-index"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('decrease_quantity/<int:id>', views.decrease_quantity, name="decrease_quantity"),
    path('increase_quantity/<int:id>', views.increase_quantity, name="increase_quantity"),
    path('delete_row/<int:id>', views.delete_row, name="delete_row"),
]