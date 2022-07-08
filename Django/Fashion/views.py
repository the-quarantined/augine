from django.shortcuts import render
# Create your views here.


# logic and functions to be written here

def home(request):
    return render(request, 'home.html')


def AddProduct(request):
    if request.method == "POST":
        print("hello")
    return render(request, 'addProd.html')
