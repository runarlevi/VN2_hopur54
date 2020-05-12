from django.contrib.auth.models import User
from django.db import models

from products.models import Product
#from user.models import Profile

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product_id)

    def get_total_item_price(self):
        return self.quantity * self.product.price

class CheckoutForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)