# Generated by Django 3.1.5 on 2021-04-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0013_auto_20210403_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, default='dish.jpg', null=True, upload_to='images/'),
        ),
    ]
