# Generated by Django 5.0.6 on 2024-07-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_order_date_shipped'),
    ]

    operations = [
        migrations.CreateModel(
            name='gpay_scanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gpay_scanner')),
            ],
        ),
    ]
