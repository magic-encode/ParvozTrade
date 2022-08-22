from django.contrib import admin
from flightapp.models.products import Products, Banner, BannerLeft
from flightapp.models.catagory import Categories


admin.site.register(Banner)
admin.site.register(Products)
admin.site.register(BannerLeft)
admin.site.register(Categories)

