# Generated by Django 4.2.2 on 2023-08-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User'), ('MENDATOR', 'Mendator')], default='User', max_length=20),
        ),
    ]