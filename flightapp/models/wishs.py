from django.db import models

from flightapp.models.products import Products

from users.models import CustomUser


class WishModel(models.Model):
    user     = models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    products = models.ManyToManyField(Products,blank=True, related_name='wishlist')
