from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999)
    name = models.CharField(max_length=150, default='name missing')
    email = models.EmailField(blank=True)
