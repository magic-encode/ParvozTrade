from django.db import models




class Post(models.Model):
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    video = models.URLField(verbose_name='video', null=True, blank=True)
    titile = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField(verbose_name='blog matni')
    aforizm = models.TextField(blank=True, null=True, verbose_name='aqilli gaplar')
    author = models.CharField(max_length=255, blank=True, null=True, verbose_name='aforizm egasi')
    time = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.titile
