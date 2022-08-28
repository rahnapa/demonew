from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Categery, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Categery,slug=c_slug)
        products_list=Product.objects.all().filter(categery=c_page,available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request,"categery.html",{'categery':c_page,'products':products})
def prodDetail(request,c_slug,product_slug):
    try:
         product=Product.objects.get(categery__slug=c_slug,slug=product_slug)
    except Exception  as e:
        raise e
    return render(request,"product.html",{'product':product})