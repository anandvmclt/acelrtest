# Cart/views.py
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .cart import Cart
from .forms import CheckoutForm
from order.views import checkout
import uuid

User = get_user_model()

# Checkout Processing function. This will convert cart items to order
def cart_detail(request):
    cart = Cart(request)
    myuuid = uuid.uuid4()
    ord_id = str(myuuid) # generate a Unique Random string for OrderID

    if request.method == 'POST':
        # form = CheckoutForm(request.POST)

        try:   # Get Username from Checkout form and find the user without login and process the order
            user_name = request.POST['user_name']
            discount = request.POST['discount']
            user = User.objects.get(username=user_name)
            email = user.email
            mobile = user.mobile
            address = user.address
            orderid = ord_id
            try:
                discount = float(discount)
            except:
                discount = 0

            if discount > 0:  # Check for ANy Discount is Applied
                total_amount = cart.get_total_cost()
                amount = total_amount * (1 - (discount / 100))
            else:
                disc = 0  # If there is No discount applied, Consider Discount as Zero percentage
                amount = cart.get_total_cost()
            order = checkout(request, user, email, address, mobile,
                             orderid, discount, amount)
            cart.clear()

            return redirect('cart:success')
        except Exception as e:  # Show Error Message to user
            messages.error(request, 'There was something error with order placement')
            return redirect('cart:cart')

    else:
        form = CheckoutForm()

        remove_from_cart = request.GET.get('remove_from_cart', '')
        change_quantity = request.GET.get('change_quantity', '')
        quantity = request.GET.get('quantity', 0)

        if remove_from_cart:
            cart.remove(remove_from_cart)
            return redirect('cart:cart')

        if change_quantity:
            cart.add(change_quantity, quantity, True)
            return redirect('cart:cart')
        return render(request, 'cart/cart.html', {'form': form})


# Call the Sucess URL
def success(request):
    messages.success(request, 'Order Placed Succesfully')
    return render(request, 'cart/success.html')
