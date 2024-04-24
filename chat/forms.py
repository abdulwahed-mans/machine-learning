# chat/forms.py
from django import forms

class ProductForm(forms.Form):
    product_name = forms.CharField(label='Enter the product name or description', max_length=100)
