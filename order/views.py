#Orders / Views.py
from django.shortcuts import render
from cart.cart import Cart
from .models import Order, OrderItem
from product.models import Product


def checkout(request, user, email, address, mobile, orderid, discount, amount):
    order = Order.objects.create(user=user, email=email, address=address,
                                  mobile=mobile, paid_amount=amount,orderid=orderid)

    for item in Cart(request):
        if discount > 0: # Check for ANy Discount is Applied
            disc = float(discount)
            total_amount = item['product'].price
            price = total_amount*(1 - (disc/100))
        else:
            disc = 0    # If there is No discount applied, Consider Discount as Zero percentage
            price = item['product'].price

        OrderItem.objects.create(order=order,discount=disc, product=item['product'],
                                price=price, quantity=item['quantity'])

        product_code =  item['product'].code   # Get Orderd Product objet via Code
        product_obj = Product.objects.get(code=product_code)
        product_stocke = product_obj.inventory
        orderd_quantity = int(item['quantity'])
        new_stock = product_stocke - orderd_quantity
        product_obj.inventory = new_stock # Update Product Stock in inventory
        product_obj.save()

    return order