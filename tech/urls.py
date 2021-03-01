from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('productDetail/<int:id>', views.productDetail, name='detail'),
]