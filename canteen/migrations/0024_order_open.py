# Generated by Django 3.1.5 on 2021-05-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0023_auto_20210429_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]
