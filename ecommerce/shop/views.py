from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Product, CartItem, Order
from .serializers import ProductSerializer, CartItemSerializer,OrderSerializer


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request):
        product_id = request.GET.get('id')
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'product_detail.html', {'product': product})


@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        return redirect('view-cart')


@method_decorator(login_required, name='dispatch')
class ViewCart(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)

        total_price = sum(item.product.price * item.quantity for item in cart_items)

        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


class CheckoutView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items:
            return redirect('view-cart')

        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'checkout.html', {'total_amount': total_amount, 'cart_items': cart_items})

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items.exists():
            total = sum(item.product.price * item.quantity for item in cart_items)
            order = Order.objects.create(user=request.user, total_amount=total)
            order.items.set(cart_items)
            cart_items.delete()
            return render(request, 'order_confirmed.html', {'order': order})
        return redirect('view-cart')


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get(self, request):
        product_id = request.GET.get('id')
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity += int(quantity)
        cart_item.save()

        return JsonResponse({"message": "Product added to cart successfully."})


class ViewCartAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can view the cart

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)


class CheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items.exists():
            total = sum(item.product.price * item.quantity for item in cart_items)
            order = Order.objects.create(user=request.user, total_amount=total)
            order.items.set(cart_items)
            cart_items.delete()
            return JsonResponse({"message": "Order confirmed", "order_id": order.id, "total_amount": total})
        return JsonResponse({"message": "Cart is empty"}, status=400)


class OrderConfirmationAPIView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

