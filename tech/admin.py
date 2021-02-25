from django.contrib import admin
from .models import TechType, Product, Review

# Register your models here.
admin.site.register(TechType)
admin.site.register(Product)
admin.site.register(Review)