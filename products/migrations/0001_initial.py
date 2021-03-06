# Generated by Django 3.2.5 on 2021-07-16 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at ')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'product tag',
                'verbose_name_plural': 'product tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('short_description', models.TextField(verbose_name='short description')),
                ('long_description', models.TextField(verbose_name='long description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.categorymodel', verbose_name='category')),
                ('tags', models.ManyToManyField(related_name='products', to='products.ProductTagModel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
