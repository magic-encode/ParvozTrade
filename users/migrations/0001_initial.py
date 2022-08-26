# Generated by Django 3.2.12 on 2022-08-25 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('video', models.URLField(blank=True, null=True, verbose_name='video')),
                ('titile', models.CharField(max_length=255)),
                ('body', models.TextField(verbose_name='blog matni')),
                ('aforizm', models.TextField(blank=True, null=True, verbose_name='aqilli gaplar')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='aforizm egasi')),
                ('data', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
