from django.shortcuts import render
from .models import Product,Comment
from django.db.models import F,Q

# Create your views here.

def homeview(request):
    Product.objects.filter(Q(pro_name__contains="a") & Q(price__gte=10000))

    return render(request,'home.html')