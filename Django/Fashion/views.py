from unicodedata import category
from django.shortcuts import render
# Create your views here.
from .models import Product

# logic and functions to be written here


def home(request):
    return render(request, 'home.html')


def AddProduct(request):
    if request.method == "POST":
        prodname = request.POST.get('prodname')
        price = request.POST.get('price')
        category = request.POST.get('category')
        desc = request.POST.get('description')
        # file = request.POST.get('image')
        prod = Product(name=prodname, price=price,
                       category=category, desc=desc)
        prod.save()
    return render(request, 'addProd.html')


def showCategories(request):
    allProds = Product.objects.all()
    category = {}
    for prod in allProds:
        if prod.category in category:
            category[prod.category].append(prod.name)
        else:
            print(type(prod.category))
            category[prod.category] = []
            category[prod.category].append(prod.name)
    # print(type(category))
    return render(request, 'categories.html', {'category': category})
