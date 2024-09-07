from django.db import models
from ProductApp.models import Product, Category
from UserApp.models import ShopieUser

class Order(models.Model):
    STATE_CHOICES = [
        ('In-Delivery', 'In-Delivery'),
        ('Delivered', 'Delivered'),
        ('Recieved', 'Recieved'),
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
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
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductApp.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)