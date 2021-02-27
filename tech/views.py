from django.shortcuts import render
from .models import Product, TechType, Review

# Create your views here.
def index(request):
    return render(request, 'tech/index.html')

def products(request):
    product_list=Product.objects.all()
    return render(request, 'tech/products.html', {'product_list': product_list})