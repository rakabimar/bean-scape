from django.forms import ModelForm
from main.models import Product

class ProductRequestForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'bitterness']