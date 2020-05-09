from django.db import models
from django.utils.deconstruct import deconstructible

from products.models import Product
from user.models import Profile

class ShoppingCart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return str(self.product_id)

class CheckoutForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)