from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/storeinfo
    path('', views.index, name="store-info-index"),
]