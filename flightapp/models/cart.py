from django.db import models
from django.db.models import Sum
from flightapp.models.products import Products
from django.contrib.auth import get_user_model

User = get_user_model()



class Cart(models.Model):
    user     = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Products,blank=True, related_name='products')
    
    @property
    def getTotalCost(self):
        return self.products.all().aggregate(Sum('price'))