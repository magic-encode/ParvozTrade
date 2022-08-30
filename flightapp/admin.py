from django.contrib import admin

from flightapp.models.cart import Cart
from flightapp.models.wishlist import Wishlist

from flightapp.models.products import Brand 
from flightapp.models.products import Banner
from flightapp.models.products import Products
from flightapp.models.products import Comments
from flightapp.models.products import SubComments
from flightapp.models.products import FeatureLeft
from flightapp.models.products import BannerLefts
from flightapp.models.products import FeatureRights

from flightapp.models.order_history import OrderHistory

from flightapp.models.category import Categories

admin.site.register(Cart)
admin.site.register(Brand)
admin.site.register(Banner)
admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Wishlist)
admin.site.register(Categories)
admin.site.register(BannerLefts)
admin.site.register(SubComments)
admin.site.register(FeatureLeft)
admin.site.register(OrderHistory)
admin.site.register(FeatureRights)

