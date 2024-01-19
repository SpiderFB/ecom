from django.urls import path
from .import views

urlpatterns = [
   path('', views.item, name=""),
   path('home/', views.item, name=""),
   path('table/', views.table, name=""),
   path('additem/', views.additem, name=""),
   path('itemdetails/<int:pk>/', views.itemdetails, name=""),
]