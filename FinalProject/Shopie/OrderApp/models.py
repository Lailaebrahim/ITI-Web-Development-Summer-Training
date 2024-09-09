from django.db import models
from ProductApp.models import Product, Category
from UserApp.models import ShopieUser

class Order(models.Model):
    STATE_CHOICES = [
        ('In-Delivery', 'In-Delivery'),
        ('Delivered', 'Delivered'),
        ('Recieved', 'Recieved'),
    ]
    state = models.CharField(
        max_length=20, choices=STATE_CHOICES, default='In-Delivery')
    created_at = models.DateTimeField(auto_now_add=True)
    GOVERNORATE_CHOICES = [
        ('Cairo', 'Cairo'),
        ('Alexandria', 'Alexandria'),
        ('Giza', 'Giza'),
        ('Mansoura', 'Mansoura')
    ]
    delivery_destination = models.CharField(max_length=100, choices=GOVERNORATE_CHOICES)
    user = models.ForeignKey(ShopieUser, on_delete=models.CASCADE, related_name='orders')

class OrderProducts(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="order_products")
    product = models.ForeignKey(
        'ProductApp.Product', on_delete=models.CASCADE, related_name="order_products")
    quantity = models.PositiveIntegerField(default=1)
    

class Cart(models.Model):
    user = models.OneToOneField(ShopieUser, on_delete=models.CASCADE, related_name='cart')
  
class CartProducts(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(
        'ProductApp.Product', on_delete=models.CASCADE,null=True, related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1)