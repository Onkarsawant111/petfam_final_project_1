# Generated by Django 5.0.6 on 2024-07-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_customers_phone_alter_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
