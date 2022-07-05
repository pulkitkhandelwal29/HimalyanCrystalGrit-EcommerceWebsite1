from django.shortcuts import render
from store.models import Product
from banner.models import Banner

def home(request):
    products = Product.objects.all().filter(is_available=True)
    banners = Banner.objects.all()

    context = {
    'products' : products,
    'banners' : banners,
    }

    return render(request, 'index.html',context)



def contact(request):
    return render(request,'contact.html')



def follow(request):
    return render(request,'follow.html')

def faq(request):
    return render(request,'faq.html')
