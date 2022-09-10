# Generated by Django 3.2.12 on 2022-09-10 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flightapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('tag', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, max_length=500, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='GetInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250, null=True)),
                ('phone', models.PositiveBigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='mahsulotning nomi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='mahsulot haqida qisqacha')),
                ('price_old', models.FloatField(blank=True, max_length=100, null=True, verbose_name='mahsulotning eski narxi')),
                ('price_new', models.FloatField(verbose_name='mahsulotning yangi narxi')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Chegirma')),
                ('image', models.ImageField(blank=True, default='banner_1.jpg', upload_to='', verbose_name='450x200')),
                ('is_ordered', models.BooleanField(default=False, verbose_name='is_ordered')),
                ('status', models.CharField(blank=True, choices=[('new', 'NEW'), ('sale', 'SALE')], max_length=50, null=True, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True, verbose_name='weight')),
                ('olchami', models.CharField(blank=True, max_length=255, null=True, verbose_name='olchami')),
                ('materials', models.CharField(blank=True, max_length=255, null=True, verbose_name='materials')),
                ('other_info', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='flightapp.categories')),
            ],
        ),
        migrations.CreateModel(
            name='WishModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, related_name='wishlist', to='flightapp.Products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='post',
            name='userd',
        ),
        migrations.DeleteModel(
            name='CommentsBlog',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Post',
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
