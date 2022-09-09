from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255, null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Post(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    video = models.URLField(verbose_name='video', null=True, blank=True)
    video_img = models.ImageField(
        verbose_name='video_img', null=True, blank=True)
    userd = models.OneToOneField(CustomUser, on_delete=models.PROTECT)
    text = models.TextField(verbose_name='blog matni')
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(f"ID-{self.id} {self.title}")


class CommentsBlog(models.Model):
    item = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commenting", null=True, blank=True)
    person = models.ForeignKey(
        CustomUser, related_name="usering", on_delete=models.DO_NOTHING, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
