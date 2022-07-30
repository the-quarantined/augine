from django import forms
from . models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name',
                  'price', 'category', 'desc', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control newClass'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def get_success_url(self):
    #     return reverse('addProd', args=[str(self.id)])
