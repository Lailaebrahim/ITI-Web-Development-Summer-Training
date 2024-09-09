from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart, name="cart"),
    path('order/', PlaceOrder, name="order"),
    path('order/<int:pk>', OrderDetails.as_view(), name="order_details"),
    path('ajax/check-quantity/', CheckQuantity, name="checkQuantity"),
    path('ajax/minuscheckQuantity', minusCheckQuantity, name="minusCheckQuantity"),
]
