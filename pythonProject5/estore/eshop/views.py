from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import *
from django.views.generic import ListView, DetailView, CreateView

from .serializers import ProductSerializer, OrderSerializer, CustomerSerializer


class ProductsListView(ListView):

    """Display a list of Products(:model: `eshop.Product`)"""

    template_name = 'eshop/store.html'
    context_object_name = 'products'
    queryset = Product.objects.all


class ProductDetailsView(DetailView):

    """Display selected Product(:model: `eshop.Product`)"""

    template_name = 'eshop/product-details.html'
    model = Product


class OrdersListview(LoginRequiredMixin, ListView):

    """Display list of Orders(:model: `eshop.Order`)"""

    template_name = 'eshop/order-list.html'
    queryset = (
        Order.objects.select_related('customer').prefetch_related('product')
    )


class OrderCreateView(CreateView):
    """Create Order"""
    model = Order
    fields = 'customer', 'product', 'delivery_address'
    success_url = reverse_lazy('eshop:orders')


class ProductViewSet(ModelViewSet):
    """
    A set of views for actions on Product
    Full CRUD for product entities
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = [
        'title',
        'price',

    ]
    filterset_fields = [
        'title',
        'price',
    ]
    ordering_fields = [
        'pk',
        'title',
        'description',
        'price',
    ]


class OrderViewSet(ModelViewSet):
    """
    A set of views for actions on Order
    Full CRUD for product entities
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = [
        'delivery_address',

    ]
    filterset_fields = [
        'delivery_address',
    ]
    ordering_fields = [
        'pk',
        'delivery_address',
        'customer',
        'product',
    ]


class CustomerViewSet(ModelViewSet):
    """
    A set of views for actions on Customer
    Full CRUD for product entities
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = [
        'name',
        'last_name',

    ]
    filterset_fields = [
        'name',
        'last_name',
    ]
    ordering_fields = [
        'name',
        'last_name',
        'phone_number',
        'email',
        'address',
    ]

