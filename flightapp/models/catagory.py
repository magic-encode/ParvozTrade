from django.db import models



class Banner(models.Model):
    name = models.CharField(max_length=255, verbose_name="mahsulotning nomi")
    image = models.ImageField(verbose_name='450x200', blank=True, default="banner_1.jpg")
    price = models.FloatField(verbose_name="mahsulotning narxi")
    
    def __str__(self) -> str:
        return self.name
    
    
    
    
    
    
    
    