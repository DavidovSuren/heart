# Generated by Django 4.1.5 on 2023-05-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_food_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
    ]