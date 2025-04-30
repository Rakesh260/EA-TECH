from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    AddToCartAPIView,
    ViewCartAPIView,
    CheckoutAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    OrderConfirmationAPIView, AddToCartView, ViewCart, CheckoutView
)

urlpatterns = [

    path('products/', ProductListView.as_view(), name='product-list'),
    path('product-detail/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/view/', ViewCart.as_view(), name='view-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),


    path('api/products/', ProductListAPIView.as_view(), name='api-product-list'),
    path('api/product-detail/', ProductDetailAPIView.as_view(), name='api-product-detail'),
    path('api/cart/add/', AddToCartAPIView.as_view(), name='api-add-to-cart'),
    path('api/cart/view/', ViewCartAPIView.as_view(), name='api-view-cart'),
    path('api/checkout/', CheckoutAPIView.as_view(), name='api-checkout'),
    path('api/order/<int:order_id>/confirmation/', OrderConfirmationAPIView.as_view(), name='api-order-confirmation'),
]
