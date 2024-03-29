# Generated by Django 3.2.12 on 2022-09-13 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flightapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='flightapp.categories'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='history_products', to='flightapp.Products'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='flightapp.products'),
        ),
        migrations.AddField(
            model_name='comments',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='flightapp.Products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
