# Generated by Django 3.2.5 on 2021-09-15 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210811_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='title_en',
            field=models.CharField(max_length=32, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_ru',
            field=models.CharField(max_length=32, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_uz',
            field=models.CharField(max_length=32, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_en',
            field=models.TextField(null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_ru',
            field=models.TextField(null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_uz',
            field=models.TextField(null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
    ]
