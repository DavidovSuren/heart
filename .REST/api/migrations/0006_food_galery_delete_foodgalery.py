# Generated by Django 4.1.5 on 2023-02-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_showphoto_foodgalery'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='galery',
            field=models.FileField(default='', upload_to='upload'),
        ),
        migrations.DeleteModel(
            name='FoodGalery',
        ),
    ]
