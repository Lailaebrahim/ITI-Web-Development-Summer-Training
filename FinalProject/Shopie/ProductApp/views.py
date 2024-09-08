from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import Product, Category


def home(request):
    products = Product.objects.all()[:9]
    return render(request, 'ProductApp/home.html', context={"products": products})


def AllProductsView(request):
    products = Product.objects.all()
    products_pagintaor_obj = Paginator(products, 6)
    page_num = request.GET.get('page')
    products = products_pagintaor_obj.get_page(page_num)
    return render(request, 'ProductApp/products.html', context={"products": products})

def CategoryProductsView(request):
    categories = Category.objects.all()
    categories_paginator_obj = Paginator(categories, 4)
    page_num = request.GET.get('page')
    categories_page = categories_paginator_obj.get_page(page_num)
    category_products = {}
    for category in categories_page:
        category_products[category] = Product.objects.filter(category=category)[:3]
    return render(request, 'ProductApp/category_products.html', context={"category_products": category_products, "categories_page": categories_page})

def CategoryView(request):
    category = request.GET.get('category')
    category = Category.objects.get(id=category)
    category_products = Product.objects.filter(category=category.id)
    category_products_pag_obj = Paginator(category_products, 6)
    page_num = request.GET.get('page')
    category_products_page = category_products_pag_obj.get_page(page_num)
    return render(request, 'ProductApp/category.html', context={"category_products": category_products_page, "category": category})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ProductApp/product.html'
    context_object_name = 'product'