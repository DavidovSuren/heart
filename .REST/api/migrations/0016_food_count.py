# Generated by Django 4.1.5 on 2023-05-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_food_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
