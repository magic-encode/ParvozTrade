# Generated by Django 3.2.12 on 2022-08-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0007_dayoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayoffer',
            name='image',
            field=models.ImageField(default=12, upload_to=''),
            preserve_default=False,
        ),
    ]
