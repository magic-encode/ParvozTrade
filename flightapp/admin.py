from django.contrib import admin
from flightapp.models.products import Products
from flightapp.models.catagory import Categories


admin.site.register(Categories)
admin.site.register(Products)
