# Generated by Django 3.2.12 on 2022-09-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='is_ordered',
        ),
        migrations.AlterField(
            model_name='products',
            name='price_new',
            field=models.IntegerField(verbose_name='mahsulotning yangi narxi'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_old',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='mahsulotning eski narxi'),
        ),
    ]
