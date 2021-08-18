from django.urls import path 
from myapp.views import home, search
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path('search', search, name='search')
]
