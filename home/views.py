from django.shortcuts import render, HttpResponse
from .models import allitem

# Create your views here.
def item(request):
    # return HttpResponse("At Home")
    return render(request, 'home/home.html')
    # name = request.GET.get('name', '')  # 获取请求参
    