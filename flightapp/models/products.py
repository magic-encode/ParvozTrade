from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from flightapp.models.catagory import Categories


User = get_user_model()


class Products(models.Model):

    STATUS = (
        ('new', 'NEW'),
        ('sale', 'SALE'),
    )


    name = models.CharField(max_length=255, verbose_name="mahsulotning nomi")
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
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

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name


class BannerLefts(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name



class FeatureRights(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price_old = models.FloatField(verbose_name="mahsulotning eski narxi")
    price_new = models.FloatField(verbose_name="mahsulotning yangi narxi")
    
    predecessor = models.CharField(max_length=255, default=None)
    supporttype = models.CharField(max_length=255, default=None)
    cushioning = models.CharField(max_length=255, default=None)
    totalweight = models.CharField(max_length=255, default=None)
    
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length=255, null=True, blank=True)    
    
    