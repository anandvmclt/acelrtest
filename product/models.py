# Products/Models.py
from django.db import models


# There is only one Blank field in the give sheet, which is price.

class Product(models.Model):
    name = models.CharField(max_length=180)
    code = models.CharField(max_length=20)
    price = models.FloatField(null=True, blank=True)
    features = models.TextField(max_length=200)
    inventory = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    slug = models.SlugField(max_length=140, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
