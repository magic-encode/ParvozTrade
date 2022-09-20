from django.db import models
from django.db.models import Sum

from users.models import CustomUser


class Cart(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    products = models.ManyToManyField('Products',blank=True, related_name='products')
    
    @property
    def getTotalCost(self):
        return self.products.all().aggregate(Sum('price'))


    
class Categories(models.Model):
    ALL = 0
    KUN_TAKLIFLARI=1
    ENG_KOP_SOTILADIGAN=2
    YANGILAR=3
    SIZ_UCHUN_TAVFSIYA=4
    BOSHQALAR=5
    ENG_MASHHUR_MAHSULOTLAR=6
   
    name = models.CharField(max_length=30, null=True, blank=False)
    tag  = models.CharField(max_length=30, null=True, blank=False)
    
    def __str__(self):
        return str(f"ID-{self.id} {self.name}")  
    
    
class CustomerModel(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=14, blank=False)    
    
    

class OrderHistory(models.Model):
    user     = models.OneToOneField(CustomUser, related_name='history_order', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField('Products',blank=True, related_name='history_products')   
    


class Products(models.Model):

    STATUS = (
        ('new', 'NEW'),
        ('sale', 'SALE'),
    )

    name = models.CharField(max_length=255, verbose_name="mahsulotning nomi")
    description = models.TextField(
        null=True, blank=True, verbose_name="mahsulot haqida qisqacha")
    price_old = models.IntegerField(
       verbose_name="mahsulotning eski narxi", null=True, blank=True)
    price_new = models.IntegerField(verbose_name="mahsulotning yangi narxi")
    discount = models.IntegerField(
        verbose_name="Chegirma", blank=True, null=True)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="category")
    image = models.ImageField(
        verbose_name='450x200', blank=True, default="banner_1.jpg")
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
    brend = models.CharField(
        max_length=255, verbose_name="brend", null=True, blank=True)
    other_info = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f"/page/{self.id}/"


class Comments(models.Model):
    item = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="comment", null=True, blank=True)
    person = models.ForeignKey(
        CustomUser, related_name="user", on_delete=models.DO_NOTHING, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    

class GetInfo(models.Model):
    fullname = models.CharField(max_length=250, null=True, blank=False)
    phone = models.PositiveBigIntegerField()
    message = models.TextField(blank=False)
    

    def __str__(self) -> str:
        return self.fullname  
    
    
class WishModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="wishing", null=True, blank=True)
    products = models.ManyToManyField(Products,blank=True, related_name='wishlist')    
    