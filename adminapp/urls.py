#Adminapp/Urls.py

from django.urls import path
from .views import *
app_name = 'adminapp'

urlpatterns = [
    path('', adminHome, name="home"),
    path('search/', search, name="search"),
    path('listusers', listUsers, name="listusers"),
    path('<pk>/update', UserUpdateView.as_view()),
    path('logout', logout, name="logout"),
    path('order', listOrders, name="order"),
]
