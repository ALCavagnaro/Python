# Generated by Django 4.1 on 2022-08-20 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_coderhouse', '0004_alter_familiar_cumpleanios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='edad',
        ),
    ]