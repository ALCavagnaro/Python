# Generated by Django 4.1 on 2022-08-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_coderhouse', '0002_rename_cumpleaños_familiar_cumpleanios'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='parentesco',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]