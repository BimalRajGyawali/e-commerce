from django.contrib import admin
from .models import Category, Product, Item, User, Order


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(User)
