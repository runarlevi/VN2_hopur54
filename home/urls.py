from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/home
    path('', views.index, name="home-index"),

]