from django.shortcuts import render, HttpResponse,redirect
from .models import allitem
import os
from .forms import AddItemForm

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
    # try:
    #     one_item = allitem.objects.get(product_id=pk)
    #     print("one item id =",one_item)
    # except allitem.DoesNotExist:
    # # handle the exception here
    #     print('item not found')
    #     return redirect('/')
    # return render(request, 'home/itemdetails.html', {'one_item': one_item})
    all_item = allitem.objects.get(product_id=pk)
    return render(request, 'home/itemdetails.html', {'one_item': all_item})
