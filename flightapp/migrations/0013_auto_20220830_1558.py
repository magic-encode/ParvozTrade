# Generated by Django 3.2.12 on 2022-08-30 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0012_rename_body_comments_mes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='prod',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='subcomments',
            old_name='prod',
            new_name='products',
        ),
    ]