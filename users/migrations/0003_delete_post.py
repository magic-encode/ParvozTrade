# Generated by Django 3.2.12 on 2022-08-25 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_post_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
