# Generated by Django 2.0.2 on 2019-01-08 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassName',
            new_name='Job',
        ),
    ]
