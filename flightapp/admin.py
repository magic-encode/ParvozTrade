from django.contrib import admin

from flightapp.models.cart import Cart
from flightapp.models.wishs import WishModel

from flightapp.models.products import Products
from flightapp.models.products import Comments

from flightapp.models.order_history import OrderHistory

from flightapp.models.category import Categories

admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(WishModel)
admin.site.register(Categories)
admin.site.register(OrderHistory)