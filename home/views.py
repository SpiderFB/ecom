from django.shortcuts import render, HttpResponse,redirect
from .models import allitem
import os
from .forms import AddItemForm
from django.contrib.auth import authenticate, login

all_item = allitem.objects.all()
# Create your views here.
def item(request):

    # return HttpResponse("At Home")
    all_item = allitem.objects.all()

    image_files = []
    for filename in os.listdir('static/images/banner'):
        # if filename.endswith('.jpg') or filename.endswith('.png'):
        image_files.append(filename)

    return render(request, 'home/home.html', {'all_item': all_item, 'images': image_files})
    # name = request.GET.get('name', '')
def table(request):
    all_item = allitem.objects.all()
    return render(request, 'home/table.html', {'all_item': all_item})

def additem(request):
    # return HttpResponse("okay ")
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'home/table.html', {'all_item': all_item})
        else:
            form = AddItemForm()
        return render(request, 'home/additem.html', {'form': form})
def itemdetails(request, pk):
    all_item = allitem.objects.get(product_id=pk)
    return render(request, 'home/itemdetails.html', {'one_item': all_item})
def user_login(request):
    return render(request,'home/login.html')
    # return HttpResponse("okay ")

def auth(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            # Display an error message
            error_message = "Invalid username or password"
            return render(request, 'home/login.html', {'error_message': error_message})
    else:
        # Display the login form
        return render(request, 'home/login.html')

    