# Generated by Django 3.0 on 2019-12-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
