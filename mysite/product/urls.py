from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeProduct.as_view(), name='home'),
    path('category/<int:category_id>/', ProductByCategory.as_view(), name='category'),
    path('product/<int:pk>/', ViewProduct.as_view(), name='view_product'),
    path('product/add_product/', CreateProduct.as_view(), name='add_product'),
]
