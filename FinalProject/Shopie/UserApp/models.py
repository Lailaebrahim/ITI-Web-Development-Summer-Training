from django.db import models
from django.contrib.auth.models import User


class ShopieUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopieuser')
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='Users/', default='Users/default.png')
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username