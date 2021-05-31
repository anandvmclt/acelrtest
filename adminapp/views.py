# AdminApp/Views.py
from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import logout as django_logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .forms import CustomUserChangeForm
from order.models import OrderItem

User = get_user_model()


# Search user by name and mobile
@login_required()
def search(request):
    query = request.GET.get('query', '')
    users = User.objects.filter(Q(first_name__icontains=query) | Q(mobile__icontains=query))

    return render(request, 'adminapp/search.html', {'users': users, 'query': query})


# Admin Home Page
@login_required()
def adminHome(request):
    return render(request, 'adminapp/home.html')


# Lias all users
@login_required()
def listUsers(request):  # List all Customers
    users = User.objects.filter(is_staff=False)
    context = {'users': users}
    return render(request, 'adminapp/users.html', context)


# Update User
class UserUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    model = User
    template_name = 'adminapp/update_user.html'
    success_message = 'User successfully Updated!'
    success_url = reverse_lazy('adminapp:listusers')


# List all Orders
@login_required()
def listOrders(request):  # List all Customers
    orders = OrderItem.objects.all()
    context = {'orders': orders}
    return render(request, 'adminapp/orders.html', context)


# Logout function
def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    django_logout(request)
    return redirect('adminapp:home')
