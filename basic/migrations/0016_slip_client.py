# Generated by Django 3.0.8 on 2020-11-27 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0015_auto_20201127_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='slip',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Client'),
        ),
    ]