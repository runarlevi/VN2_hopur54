from django.db import models
from products.models import Product
from user.models import Profile

class ShoppingCart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(Product.price)
    quantity = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return str(self.product_id)
