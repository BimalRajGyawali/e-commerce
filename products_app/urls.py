from django.urls import path

from products_app.views import index


urlpatterns = [path('', index, name='index')]


