from django.shortcuts import render, HttpResponse
from .models import allitem
import os
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