from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

#Create your models here

class SearchHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


