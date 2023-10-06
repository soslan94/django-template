from django.urls import path, include
from .views import ProductsListView, OrdersListview, ProductDetailsView, OrderCreateView, ProductViewSet, OrderViewSet, \
    CustomerViewSet
from rest_framework.routers import DefaultRouter


app_name = 'eshop'

routers = DefaultRouter()
routers.register('products', ProductViewSet)
routers.register('orders', OrderViewSet)
routers.register('customers', CustomerViewSet)


urlpatterns = [
    path('', ProductsListView.as_view(), name='store'),
    path('api/', include(routers.urls)),
    path('orders/', OrdersListview.as_view(), name='orders'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='products_details'),
    path('orders/create', OrderCreateView.as_view(), name='order_create'),
]
