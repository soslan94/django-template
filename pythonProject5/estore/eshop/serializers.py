from rest_framework import serializers

from .models import Product, Order, Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'name',
            'last_name',
            'phone_number',
            'email',
            'address',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'pk',
            'title',
            'description',
            'price',
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'pk',
            'delivery_address',
            'order_date',
            'customer',
            'product',
        )