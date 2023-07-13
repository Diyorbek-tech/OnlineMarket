from django.shortcuts import render
from .models import Product,Comment
from django.db.models import F,Q

# Create your views here.

def homeview(request):

    context={
        'products':Product.objects.all()
    }

    return render(request,'home.html',context=context)


def singlepro_view(request,slug):
    context = {
        'single': Product.objects.get(slug=slug)
    }
    return render(request,'single_pro.html',context=context)


