
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import allitem


class AddItemForm(forms.ModelForm):
    class Meta:
        model = allitem
        fields = ['product_name', 'product_description', 'product_category', 'product_price', 'product_quantity', 'product_image']

        widgets = {
            'product_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control'}),
            'product_category': forms.TextInput(attrs={'class': 'form-control'}),
        }