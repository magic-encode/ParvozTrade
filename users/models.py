from cgitb import text
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    video = models.URLField(verbose_name='video', null=True, blank=True)
    video_img = models.ImageField(verbose_name='video_img', null=True, blank=True)
    userd  = models.ForeignKey(User, related_name='userd', on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name='blog matni')
    aforizm = models.CharField(max_length=255, blank=True, null=True, verbose_name='aqilli gaplar')
    name_aforiz = models.CharField(max_length=255, blank=True, null=True, verbose_name='aforizm egasi')
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):          
        return str(f"ID-{self.id} {self.title}")
