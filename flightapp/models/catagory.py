from django.db import models

 
    
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
    
    