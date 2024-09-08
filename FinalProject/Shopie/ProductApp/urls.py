from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('products/', AllProductsView, name="products"),
    path('category/', CategoryProductsView, name="category_products"),
    path('products/category/', CategoryView, name="category"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product")
]
