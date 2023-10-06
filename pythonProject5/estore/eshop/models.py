from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):

    """Stores info about customers"""

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    fathers_name = models.CharField(max_length=32)
    phone_number = models.IntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    address = models.TextField(max_length=400)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    """All needed information about our products"""

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):

    """Information what helps to create order. Related to :model: `eshop.Customer` and :model: `eshop.Product`"""

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
