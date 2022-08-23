from django.db import models

 
    
class Categories(models.Model):
    ALL = 0
    ENG_KOP_SOTILADIGAN=1
    YANGILAR=2
    KUN_TAKLIFLARI=3
    SIZ_UCHUN_TAVFSIYA=4
    BOSHQALAR=5
    ENG_MASHHUR_MAHSULOTLAR=6
   

    name = models.CharField(max_length=30, null=True, blank=False)
    tag  = models.CharField(max_length=30, null=True, blank=False)
    
    def __str__(self):
        return str(f"ID-{self.id} {self.name}")   
    
    # class Meta:
    #     verbose_name=("Category")

    #     verbose_name_plural=("Categories")

    #     def __str__(self):

    #         return self.name 