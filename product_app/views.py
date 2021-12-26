from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.
def add_product(request):
    name = "Sugar"
    weight = 100
    price = 40
    product = Product(name=name, weight=weight, price=price)
    product.save(using='product')
    return HttpResponse("Product Save")