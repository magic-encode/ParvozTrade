from django.db import models
from users.models import CustomUser

class OrderHistory(models.Model):
    user     = models.OneToOneField(CustomUser, related_name='history_order', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField('Products',blank=True, related_name='history_products')