from django.db import models
from accountsApp.models import PortfolioUser
from PIL import Image


class Technology(models.Model):
    technology = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return str(self.technology)


class Contributer(models.Model):
    name = models.CharField(max_length=30)
    contribution = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='images/contributer/', default='images/contributer/default.png')
    email = models.EmailField(max_length=254, default=None)
    github_link = models.URLField()
    linkedin_link = models.URLField()
    portfolio_user = models.ForeignKey(
        PortfolioUser, on_delete=models.CASCADE, related_name='contributers')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        max_size = (500, 500)
        image.thumbnail(max_size)
        image.save(self.image.path)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='images/projects/', default='images/default.png')
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    contributers = models.ManyToManyField(Contributer)
    portfolio_user = models.ForeignKey(
        PortfolioUser, on_delete=models.CASCADE, related_name='projects')
    technologies = models.ManyToManyField(Technology)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        max_size = (500, 500)
        image.thumbnail(max_size)
        image.save(self.image.path)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class ContributerTechnology(models.Model):
    contributer = models.ForeignKey(Contributer, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
