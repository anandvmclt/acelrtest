# Cart/forms.py
from django import forms
from user.models import User


# Cart Checkoout form for adding Customer details
class CheckoutForm(forms.ModelForm):
    #user_name = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username',]
