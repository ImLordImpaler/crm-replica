# Generated by Django 3.0.5 on 2020-11-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20201122_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='others', max_length=10),
        ),
    ]
