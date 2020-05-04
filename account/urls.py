from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/account
    path('', views.index, name="account-index"),
]