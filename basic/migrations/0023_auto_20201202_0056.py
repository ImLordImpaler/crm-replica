# Generated by Django 3.0.8 on 2020-12-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0022_auto_20201202_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slip',
            name='product',
            field=models.ManyToManyField(default=None, to='basic.Product'),
        ),
        migrations.AlterField(
            model_name='slip',
            name='service',
            field=models.ManyToManyField(default=None, to='basic.Service'),
        ),
    ]
