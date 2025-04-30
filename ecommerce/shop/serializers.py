from rest_framework import serializers
from .models import Product, CartItem, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'items']
