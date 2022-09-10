
from django.db import models
from flightapp.models.category import Categories
from users.models import CustomUser


class Products(models.Model):

    STATUS = (
        ('new', 'NEW'),
        ('sale', 'SALE'),
    )

    name = models.CharField(max_length=255, verbose_name="mahsulotning nomi")
    description = models.TextField(
        null=True, blank=True, verbose_name="mahsulot haqida qisqacha")
    price_old = models.FloatField(
        max_length=100, verbose_name="mahsulotning eski narxi", null=True, blank=True)
    price_new = models.FloatField(verbose_name="mahsulotning yangi narxi")
    discount = models.IntegerField(
        verbose_name="Chegirma", blank=True, null=True)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="category")
    image = models.ImageField(
        verbose_name='450x200', blank=True, default="banner_1.jpg")
    is_ordered = models.BooleanField(verbose_name="is_ordered", default=False)
    status = models.CharField(
        max_length=50, verbose_name="status", choices=STATUS, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    weight = models.CharField(
        max_length=50, verbose_name="weight", null=True, blank=True)
    olchami = models.CharField(
        max_length=255, verbose_name="olchami", null=True, blank=True)
    materials = models.CharField(
        max_length=255, verbose_name="materials", null=True, blank=True)
    other_info = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Comments(models.Model):
    item = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="comment", null=True, blank=True)
    person = models.ForeignKey(
        CustomUser, related_name="user", on_delete=models.DO_NOTHING, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    

