# Generated by Django 4.1.1 on 2022-09-24 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_rename_firstapp_first_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='First_table',
            new_name='FirstApp',
        ),
    ]
