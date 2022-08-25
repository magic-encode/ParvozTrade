from django.db import models


class GetInfo(models.Model):
    fullname = models.CharField(max_length=250, null=True, blank=False)
    nomer = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=250, null=True, blank=False)
    message = models.TextField(blank=False)

    def __str__(self) -> str:
        return self.fullname