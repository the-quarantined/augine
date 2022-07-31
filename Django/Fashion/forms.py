from django import forms
from . models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name',
                  'price', 'category', 'desc', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control detail', 'id': 'name'}),
            'price': forms.TextInput(attrs={'class': 'form-control detail', 'id': 'price'}),
            'category': forms.TextInput(attrs={'class': 'form-control detail', 'id': 'category'}),
            'desc': forms.TextInput(attrs={'class': 'form-control detail', 'id': 'desc'}),
        }

    # def get_success_url(self):
    #     return reverse('addProd', args=[str(self.id)])
