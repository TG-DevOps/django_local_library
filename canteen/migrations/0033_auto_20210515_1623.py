# Generated by Django 3.1.5 on 2021-05-15 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0032_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.question'),
        ),
    ]
