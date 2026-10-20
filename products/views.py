
from django.shortcuts import render
from .models import Product

def new(request):
    products = Product.objects.all()
    return render(request , 'Index.html', {'products': products})


