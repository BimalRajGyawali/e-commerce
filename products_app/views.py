from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLoginForm, CreditCardForm, AddressForm
from .models import Product, OrderItem, Order, Item, Category, User, Address, CardDetails
from .serializers import OrderItemSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .decorators import login_required, logout_required


def index(request):
    products = Product.objects.all()[:2]
    categories=Category.objects.all()
    return render(request, 'products_app/index.html', {'products': products,'categories':categories})


@login_required
def cart(request):
   username = request.session.get('user')
   ordered_items = OrderItem.objects.filter(user__name=username, ordered=False)
   return render(request, 'products_app/cart.html', {'ordered_items': ordered_items})



def checkout(request):
    return render(request, 'products_app/checkout.html')


@login_required
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


@logout_required
def signup(request):
    if request.method == 'GET':
        form = UserRegistrationForm()


    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')


    return render(request, 'products_app/signup.html', {'form': form})


@logout_required
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


def logout(request):
   if 'user' in request.session.keys():
       del request.session['user']
   return redirect('index')


@login_required
def checkout(request):
    username = request.session.get('user')
    ordered_items = OrderItem.objects.filter(user__name=username, ordered=False)

    user = User.objects.get(name=username)
    if request.method == 'GET':
        address_form = AddressForm()
        card_form = CreditCardForm()


    elif request.method == 'POST':
        address_form = AddressForm(request.POST)
        card_form = CreditCardForm(request.POST)

        if address_form.is_valid() and card_form.is_valid():
            street = address_form.cleaned_data['street']
            city = address_form.cleaned_data['city']
            state = address_form.cleaned_data['state']
            zip = address_form.cleaned_data['zip']
            address = Address(state=state, street=street, city=city,zip=zip,user=user)
            address.save()

            number = card_form.cleaned_data['number']
            expiry_date = card_form.cleaned_data['expiry_date']
            cvv = card_form.cleaned_data['cvv']
            card = CardDetails(number=number, expiry_date=expiry_date,cvv=cvv, user=user)
            card.save()

            order = Order.objects.create(user=user)

            for ordered_item in ordered_items:
                ordered_item.ordered = True
                ordered_item.save()
                order.ordered_items.add(ordered_item)




            return redirect('index')



    return render(request, 'products_app/checkout.html', {'address_form': address_form, 'card_form': card_form,
                                                          'ordered_items':ordered_items})
