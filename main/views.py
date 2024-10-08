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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': request.user.username,
        'class': 'PBP E',
        'appName' : 'BeanScape',
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
            messages.error(request, "Invalid username or password. Please try again.")
        
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
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
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

@csrf_exempt
@require_POST
def add_product_ajax(request):
    user = request.user
    name = strip_tags(request.POST.get('name'))
    price = request.POST.get('price')
    description = strip_tags(request.POST.get('description'))
    category = request.POST.get('category')
    bitterness = request.POST.get('bitterness')
    
    new_product = Product(
        user=user,
        name=name,
        price=price,
        description=description,
        category=category,
        bitterness=bitterness
    )
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)