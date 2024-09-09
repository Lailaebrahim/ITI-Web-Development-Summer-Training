from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.http import Http404, JsonResponse
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from .models import *
from .forms import OrderForm


@login_required
def cart(request):
    try:
        user = request.user.shopieuser
    except ShopieUser.DoesNotExist:
        raise Http404

    product_id = request.GET.get('product')

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)

    if product_id:
        product = Product.objects.get(id=product_id)
        cart_product, created = CartProducts.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            cart_product.quantity += 1
            cart_product.save()

    return render(request, 'OrderApp/cart.html', context={"cart": cart})


@login_required
def PlaceOrder(request):
    try:
        user = request.user.shopieuser
    except ShopieUser.DoesNotExist:
        raise Http404
    cart = get_object_or_404(Cart, id=request.GET.get('cart'))
    cart_products = cart.cart_products.all()
    if not cart_products.exists():
        raise Http404
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.user = user
        order.save()
        for cart_product in cart_products:
            order_product = OrderProducts.objects.create(
                order=order,
                product=cart_product.product,
                quantity=cart_product.quantity
            )
            cart_product.delete()
            product = get_object_or_404(Product, id=cart_product.product.id)
            if product.quantityInStock < order_product.quantity:
                raise Http404
            product.quantityInStock -= order_product.quantity
            product.save()
        cart.delete()
        return redirect(reverse('order_details', kwargs={'pk': order.pk}))

    return render(request, 'OrderApp/order.html', context={"cart": cart, "form": form})


class OrderDetails(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'OrderApp/order_details.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        order_products = self.object.order_products.all()
        context['total'] = sum([order_product.product.price *
                               order_product.quantity for order_product in order_products])
        return context


def CheckQuantity(request):
    product_id = request.GET.get('productId')
    quantity = int(request.GET.get('quantity'))
    cart_id = request.GET.get('cartId')
    product = get_object_or_404(Product, id=product_id)
    if product.quantityInStock < (quantity + 1):
        data = {"state": False, "quantity": product.quantityInStock}
    else:
        cart = get_object_or_404(Cart, id=cart_id)
        if request.user.shopieuser != cart.user:
            raise PermissionDenied
        cart_product = get_object_or_404(
            CartProducts, cart=cart, product=product)
        try:
            cart_product.quantity += 1
            cart_product.save()
        except:
            raise Http404
        data = {"state": True, "quantity": cart_product.quantity}
    return JsonResponse(data)


def minusCheckQuantity(request):
    product_id = request.GET.get('productId')
    cart_id = request.GET.get('cartId')
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, id=cart_id)
    if request.user.shopieuser != cart.user:
        raise PermissionDenied
    cart_product = get_object_or_404(
        CartProducts, cart=cart, product=product)
    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.save()
        cart.save()
        data = {"state": True, "quantity": cart_product.quantity}
    else:
        cart_product.delete()
        data = {"state": False}
    return JsonResponse(data)
