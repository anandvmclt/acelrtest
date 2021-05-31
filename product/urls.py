#Products/Urls.py

from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('', views.HomePage.as_view() , name='homepage'),
    path('<str:slug>', views.HomePage.as_view() , name='quickadd'),
    path('search/', views.search, name='search'),
    path('product/<str:slug>', views.product, name='product'),
]