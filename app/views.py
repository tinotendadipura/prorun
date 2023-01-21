from django.shortcuts import render , redirect , get_object_or_404,redirect
from django.http import HttpResponse
from .models import  ContactForm ,Gallery ,Resources ,BranchLocator,Product
from django.contrib import messages
import folium 
import os 
import base64
from folium import IFrame



def home(request):
    
    return render(request , 'index.html')


def about_us(request):
    all_resource = Resources.objects.all()
    context = {'all_resource':all_resource}
    return render(request , 'about-us.html',context)

def service_industries(request):
    all_resource = Resources.objects.all()
    all_images = Gallery.objects.all()

    context = {'all_images':all_images,
    }
    return render(request , 'shop/index.html',context)

def products(request ,id):
    all_resource = Resources.objects.all()
    product_datail = Product.objects.get(id = id)
    context = { 
     'product_datail':product_datail,
     'all_resource':all_resource

    }

    return render(request , 'shop/product-details.html',context)


def services(request):
   
    return render(request , 'services.html')



def our_work(request):
     all_images = Gallery.objects.all()
    
     context = {'all_images':all_images}
     return render(request , 'our_work.html',context)



def shop(request):
    all_products = Product.objects.all()
    context = {'all_products':all_products}
    return render(request , 'shop.html',context)


def get_quote(request):
   
    return render(request , 'get-quote.html')


def contact_us(request):
    all_resource = Resources.objects.all()
    if request.method == "POST":
        fullName     = request.POST.get("name"," ")
        phone_number = request.POST.get("phone"," ")
        email        = request.POST.get("email"," ")
        city         = request.POST.get("city"," ")
        product      = request.POST.get("product"," ")
        quantity     = request.POST.get("quantity"," ")
        your_message = request.POST.get("message"," ")

        ContactForm.objects.get_or_create(
        fullName      = fullName,
        phone_number  = phone_number,
        email         = email,
        city          = city,
        product       = product,
        your_message  = your_message, 
        quantity      = quantity
          )
        messages.success(request ,'You Have Succesifully Submitted Your Request!' )


    
    context = {'all_resource':all_resource}
    return render(request , 'contact-us.html',context)



