# Generated by Django 3.1.5 on 2021-04-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0020_auto_20210417_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Cancelled',
            new_name='cancelled',
        ),
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
