from django.urls import path

from products_app.views import Index

app_name = "products_app"

urlpatterns = [path('', Index.as_view(), name='index'),
               ]