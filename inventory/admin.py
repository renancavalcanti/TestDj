from django.contrib import admin

# Register your models here.
# inventory/admin.py
from django.contrib import admin
from .models import Product

admin.site.register(Product)
