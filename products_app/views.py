from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all();
    return render(request, 'products_app/index.html', {'products': products})


def cart(request):
    return render(request, 'products_app/cart.html')


def checkout(request):
    return render(request, 'products_app/checkout.html')


def cart_save(request):
    return render(request, 'products_app/cart.html')

