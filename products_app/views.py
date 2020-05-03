from django.shortcuts import render, redirect
from .models import Product, OrderItem, Item


def index(request):
    products = Product.objects.all()[:2]
    return render(request, 'products_app/index.html', {'products': products})


def cart(request):
    ordered_items = OrderItem.objects.all()
    return render(request, 'products_app/cart.html', {'ordered_items': ordered_items})


def checkout(request):
    return render(request, 'products_app/checkout.html')


def cart_save(request, id):
    item = Item.objects.filter(id=id).first()
    quantity = request.POST.get('quantity')
    order_item = OrderItem(item=item, quantity=quantity)
    order_item.save()
    return redirect('cart')
