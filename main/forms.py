from django.forms import ModelForm, NumberInput, Select
from main.models import Product
from django.utils.html import strip_tags

class ProductRequestForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'bitterness']
        widgets = {
            'bitterness': NumberInput(attrs={
                'type': 'range',
                'min': '1',
                'max': '10',
                'class': 'w-full h-2 bg-coffee-light rounded-lg appearance-none cursor-pointer'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value for bitterness if not already set
        if not self.initial.get('bitterness'):
            self.initial['bitterness'] = 5
        self.fields['category'].widget = Select(choices=Product.CATEGORY_CHOICES)
        
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)