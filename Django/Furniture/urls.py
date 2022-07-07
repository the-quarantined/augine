from django.urls import path
from .views import home

# urls for our WebApp

urlpatterns = [
    path('', home, name='home'),
]
