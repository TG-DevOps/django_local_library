# Generated by Django 3.1.5 on 2021-05-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0030_order_paymentmode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='status',
        ),
        migrations.AddField(
            model_name='dish',
            name='discountPercent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='discountPercent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]