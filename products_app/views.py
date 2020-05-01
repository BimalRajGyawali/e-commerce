from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "products_app/index.html"