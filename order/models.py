# Order/Models.py
from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


# Table crated for Order Management
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orderd_user")
    email = models.CharField(null=True,max_length=100)
    address = models.CharField(null=True,max_length=100)
    mobile = models.CharField(null=True,max_length=100)
    orderid = models.CharField(null=True,max_length=20, unique=True)
    status = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.orderid)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    discount = models.IntegerField(default=0,null=True)

    def __str__(self):
        return '%s' % self.order

    def get_total_price(self):
        return self.price * self.quantity
