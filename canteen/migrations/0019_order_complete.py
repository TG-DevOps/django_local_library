# Generated by Django 3.1.5 on 2021-04-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0018_auto_20210411_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
