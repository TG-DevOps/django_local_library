# Generated by Django 3.1.5 on 2021-05-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0025_auto_20210501_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='confirmdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]