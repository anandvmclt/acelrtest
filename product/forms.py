# Products/Forms.py
from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
