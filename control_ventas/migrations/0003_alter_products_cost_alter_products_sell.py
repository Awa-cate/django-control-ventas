# Generated by Django 5.1.4 on 2025-01-14 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_ventas', '0002_products_cost_products_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='sell',
            field=models.IntegerField(default=0),
        ),
    ]
