from django.db import models

# Create your models here.
class Contributer(models.Model):
    name = models.CharField(max_length=30)
    contribution = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='images/contributer/', default='images/contributer/default.png')
    email = models.EmailField(max_length=254,default=None)
    github_link = models.URLField()
    linkedin_link = models.URLField()


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='images/', default='images/default.png')
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    contributers = models.ManyToManyField(Contributer)
