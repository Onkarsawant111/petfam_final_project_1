# Generated by Django 5.0.6 on 2024-07-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptcatpics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=15)),
                ('catdesc', models.CharField(max_length=100)),
                ('catimg', models.ImageField(upload_to='cat_pics')),
            ],
        ),
    ]
