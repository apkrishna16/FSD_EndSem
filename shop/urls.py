from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product_details/<int:plant_id>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
]