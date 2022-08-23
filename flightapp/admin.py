from django.contrib import admin
from flightapp.models.products import Products, Banner, BannerLefts
from flightapp.models.catagory import Categories


admin.site.register(Banner)
admin.site.register(Products)
admin.site.register(BannerLefts)
admin.site.register(Categories)

