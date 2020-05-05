from django.shortcuts import render, redirect
from .models import Product, OrderItem, Item, Category
from .serializers import OrderItemSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


def index(request):
    products = Product.objects.all()[:2]
    categories=Category.objects.all()
    return render(request, 'products_app/index.html', {'products': products,'categories':categories})


def cart(request):
    ordered_items = OrderItem.objects.all()
    return render(request, 'products_app/cart.html', {'ordered_items': ordered_items})


def checkout(request):
    return render(request, 'products_app/checkout.html')


def cart_save(request):
    id = request.GET.get('id')
    item = Item.objects.filter(id=id).first()
    quantity = request.GET.get('quantity')
    order_item = OrderItem(item=item, quantity=quantity)
    order_item.save()
    return redirect('cart')


def delete(request):
    id = request.GET.get('id')
    OrderItem.objects.filter(id=id).delete()
    return redirect('cart')


@csrf_exempt
def update(request):
    data = JSONParser().parse(request)
    serializer = OrderItemSerializer(data=data, many=True)
    if serializer.is_valid():
        items = serializer.validated_data
        for item in items:
            id, quantity = item['id'], item['quantity']
            ordered_item = OrderItem.objects.get(pk=id)
            ordered_item.quantity = quantity
            ordered_item.save()
        return JsonResponse(serializer.data, status=200, safe=False)

    return JsonResponse('Error', status=401)

