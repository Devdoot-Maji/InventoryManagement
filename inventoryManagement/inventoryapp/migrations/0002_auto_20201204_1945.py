# Generated by Django 3.1.2 on 2020-12-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyaccounts',
            name='company_account',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='companyaccounts',
            name='ifsc',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='aadhar_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='account_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ifsc',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='monthlypayment',
            name='amount',
            field=models.FloatField(),
        ),
    ]
