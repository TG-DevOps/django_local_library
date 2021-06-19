# Generated by Django 3.1.5 on 2021-03-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0009_feedback_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='status',
        ),
        migrations.AddField(
            model_name='dish',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]