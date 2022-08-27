from django.db import models
from django.db.models import Sum
from flightapp.models.products import Products

from users.models import CustomUser


class Cart(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    products = models.ManyToManyField(Products,blank=True, related_name='products')
    
    @property
    def getTotalCost(self):
        return self.products.all().aggregate(Sum('price'))