# Generated by Django 3.1.5 on 2021-04-04 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0016_auto_20210404_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='qty',
            new_name='quantity',
        ),
    ]
