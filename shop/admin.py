from django.contrib import admin
from .models import Plant, Cart, Order, OrderItem, Rating, PlantInventory

admin.site.register(Plant)
admin.site.register(Rating)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PlantInventory)
