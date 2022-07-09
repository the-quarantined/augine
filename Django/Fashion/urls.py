from django.urls import path
from .views import AddProduct, home, showCategories

# urls for our WebApp

urlpatterns = [
    path('', home, name='home'),
    path('addProd/', AddProduct, name='addProd'),
    path('categories/', showCategories, name='categories'),
]
