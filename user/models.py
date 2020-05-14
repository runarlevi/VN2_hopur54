from django.contrib.auth.models import User
from django.db import models
from products.models import Product
from datetime import datetime

DEFAULT_PROFILE_IMG = "https://static.thenounproject.com/png/258763-200.png"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    favorite_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    profile_image = models.CharField(max_length=999, default=DEFAULT_PROFILE_IMG)
    name = models.CharField(max_length=150, default='name missing')
    email = models.EmailField(blank=True)


class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, editable=False)