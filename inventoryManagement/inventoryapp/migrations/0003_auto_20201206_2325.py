# Generated by Django 3.1.2 on 2020-12-06 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_auto_20201206_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='arrival_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.arrivallocation'),
        ),
    ]
