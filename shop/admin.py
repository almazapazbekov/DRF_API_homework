from django.contrib import admin

from .models import Category, Firm, Product

admin.site.register(Category)
admin.site.register(Firm)
admin.site.register(Product)
