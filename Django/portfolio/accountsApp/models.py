from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class PortfolioUser(models.Model):
    # extend User Model in djnago using one to one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/profile/', default='images/profile/default.png')
    bio = models.TextField(max_length=300, null=True)
    jobTitle = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        max_size = (500, 500)
        image.thumbnail(max_size)
        image.save(self.image.path)

    def __str__(self) -> str:
        return self.user.username
