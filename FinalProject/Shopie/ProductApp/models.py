from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(null=False, max_length=100)
    
    def __str__(self):
        return self.category
    
    
class Product(models.Model):
    name = models.CharField(null=False, max_length=100)
    price = models.FloatField(null=False)
    description = models.TextField(null=False, max_length=500)
    image = models.ImageField(upload_to='products/', default='products/default_product.png')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantityInStock = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']