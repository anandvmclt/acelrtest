# User/Models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Table crated with Null and Blank Values as per the Given Sheet
class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, max_length=254, unique=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

