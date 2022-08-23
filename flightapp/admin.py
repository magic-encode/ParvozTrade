from django.contrib import admin

from flightapp.models.products import Brand 
from flightapp.models.products import Banner
from flightapp.models.products import Products
from flightapp.models.products import BannerLefts
from flightapp.models.products import FeatureRights

from flightapp.models.catagory import Categories


admin.site.register(Brand)
admin.site.register(Banner)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(BannerLefts)
admin.site.register(FeatureRights)

