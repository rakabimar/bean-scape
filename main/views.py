from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import ProductRequestForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    product_requests = Product.objects.filter(user=request.user)
    context = {
        'npm' : '2306123456',
        'name': request.user.username,
        'class': 'PBP E',
        'appName' : 'BeanScape',
        'product_requests': product_requests,
        'last_login': request.COOKIES.get('last_login', 'N/A')  # Use get to avoid KeyError
    }

    return render(request, "main.html", context)

def create_product_request(request):
    form = ProductRequestForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        product_request = form.save(commit=False)
        product_request.user = request.user
        product_request.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_request.html", context)

def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been successfully registered")
            return redirect('main:login')
    context = {'form': form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def edit_product(request, id):
    # Get product from id
    product = Product.objects.get(pk = id)
    
    # Set product as instance of forms
    form = ProductRequestForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == "POST":
        # Save form
        form.save()
        # Return to main page
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product from id
    product = Product.objects.get(pk = id)
    
    # Delete product
    product.delete()
    
    # Return to main page
    return HttpResponseRedirect(reverse('main:show_main'))