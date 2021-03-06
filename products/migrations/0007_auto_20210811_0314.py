# Generated by Django 3.2.5 on 2021-08-11 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_wishlistmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='products.productmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='wishlistmodel',
            unique_together={('user', 'product')},
        ),
    ]
