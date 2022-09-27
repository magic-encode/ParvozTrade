from django.contrib import admin

from .models import Cart
from .models import WishModel

from .models import Products
from .models import Comments
from .models import ReklamaView

from .models import OrderHistory

from .models import Categories

admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(WishModel)
admin.site.register(Categories)
admin.site.register(ReklamaView)
admin.site.register(OrderHistory)