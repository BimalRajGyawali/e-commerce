from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm, UserLoginForm
from .models import Product, OrderItem, Item, Category, User
from .serializers import OrderItemSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def index(request):
    products = Product.objects.all()[:2]
    categories=Category.objects.all()
    return render(request, 'products_app/index.html', {'products': products,'categories':categories})


def cart(request):
    username = request.session.get('user')
    ordered_items = OrderItem.objects.filter(user__name=username)
    return render(request, 'products_app/cart.html', {'ordered_items': ordered_items})


def checkout(request):
    return render(request, 'products_app/checkout.html')


def cart_save(request):
    username = request.session.get('user')
    user = User.objects.get(name=username)
    id = request.GET.get('id')
    item = Item.objects.filter(id=id).first()
    quantity = request.GET.get('quantity')
    order_item = OrderItem(item=item, quantity=quantity, user=user)
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



class SignUp(CreateView):
    form_class = UserRegistrationForm
    template_name = 'products_app/signup.html'
    success_url = reverse_lazy('index')


def login(request):
    if request.method == 'GET':
        form = UserLoginForm()


    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(name=username, password=password).first()
            if user is not None:
                request.session['user'] = username
                return redirect('index')

            else:
                messages.error(request, 'Username or password no matched')


    return render(request, 'products_app/login.html', {'form': form})