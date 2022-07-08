from django.urls import path
from .views import AddProduct, home

# urls for our WebApp

urlpatterns = [
    path('', home, name='home'),
    path('addProd/', AddProduct, name='addProd'),
]
