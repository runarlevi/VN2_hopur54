from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/products
    path('', views.index, name="products-index"),
    path('consoles/', views.filter_consoles, name="consoles-index"),
    path('games/', views.filter_games, name="games-index"),
    path('accessories/', views.filter_accessories, name="accessories-index"),
    path('<int:id>', views.get_product_by_id, name='product_details'),
    path('create_product', views.create_product, name='create_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart')
]