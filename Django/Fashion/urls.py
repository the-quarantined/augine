from django.urls import path
from .views import AddProduct, start, image, showCategories

# urls for our WebApp

urlpatterns = [
    path('', start, name='start'),
    path('addProd/', AddProduct.as_view(), name='addProd'),
    path('image/', image, name='image'),
    path('image/categories/<str:mssg>', showCategories, name='categories'),
]
