# Generated by Django 5.1.4 on 2025-01-15 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_ventas', '0004_products_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
