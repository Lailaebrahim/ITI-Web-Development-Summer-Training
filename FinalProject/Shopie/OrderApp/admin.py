from django.contrib import admin
from .models import Order, OrderProducts, Cart, CartProducts


admin.site.register(Order)
admin.site.register(OrderProducts)
admin.site.register(Cart)
admin.site.register(CartProducts)
