# Generated by Django 3.1.5 on 2021-04-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0011_auto_20210323_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
