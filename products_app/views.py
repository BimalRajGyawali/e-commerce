from django.shortcuts import render


def index(request):
    return render(request, 'products_app/index.html')
