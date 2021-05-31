# Product/views.py
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import AddToCartForm
from .models import Product
from cart.cart import Cart


# Create your views here.
def index(request):
    return redirect('product:homepage')


class HomePage(View):

    def get(self, request):
        all_products = Product.objects.all()[0:8]
        return render(request, 'product/frontpage.html', {'all_products': all_products})

    def post(self,request,slug):
        cart = Cart(request)
        product = get_object_or_404(Product, slug=slug)
        cart.add(product_id=product.id, quantity=1, update_quantity=False)
        messages.success(request, 'The product was added to the cart')
        return redirect('product:homepage')


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(features__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})


def product(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            messages.success(request, 'The product was added to the cart')

            url = '/shop/product/' + str(slug)
            return redirect(url)

        messages.error(request, 'The product adding failed..!')
        form = AddToCartForm()
        return render(request, 'product/product.html', {'form': form, 'product': product})

    else:
        form = AddToCartForm()
        return render(request, 'product/product.html', {'form': form, 'product': product})
