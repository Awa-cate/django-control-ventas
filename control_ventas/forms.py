from django.forms import ModelForm, DateInput
from .models import Products
from .models import Sells

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'amount', 'cost', 'sell']
        
class SellForm(ModelForm):
    class Meta:
        model = Sells
        fields = ['day', 'product', 'amount']
        widgets = {
            'day': DateInput(attrs={'type': 'date'})
        }