from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()[:9]
    return render(request, 'ProductApp/home.html', context={"products": products})
