# Generated by Django 3.1.2 on 2020-12-07 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0009_auto_20201207_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlypayment',
            name='company_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.companyaccounts'),
        ),
        migrations.AlterField(
            model_name='monthlypayment',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.employee'),
        ),
        migrations.AlterField(
            model_name='record',
            name='arrival_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.arrivallocation'),
        ),
        migrations.AlterField(
            model_name='record',
            name='checker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.checker'),
        ),
        migrations.AlterField(
            model_name='record',
            name='quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.quality'),
        ),
        migrations.AlterField(
            model_name='record',
            name='transport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventoryapp.transport'),
        ),
    ]
