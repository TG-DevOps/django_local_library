# Generated by Django 3.1.5 on 2021-05-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0031_auto_20210515_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
