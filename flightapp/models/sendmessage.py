from django.db import models

from flightapp.models.products import Products


class GetInfo(models.Model):
    fullname = models.CharField(max_length=250, null=True, blank=False)
    phone = models.PositiveBigIntegerField()
    message = models.TextField(blank=False)
    

    def __str__(self) -> str:
        return self.fullname