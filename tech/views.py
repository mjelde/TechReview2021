from django.shortcuts import render, get_object_or_404
from .models import Product, TechType, Review
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'tech/index.html')

def products(request):
    product_list=Product.objects.all()
    return render(request, 'tech/products.html', {'product_list': product_list})

def productDetail(request, id):
    product=get_object_or_404(Product, pk=id)
    return render(request, 'tech/productdetail.html', {'product' : product})

