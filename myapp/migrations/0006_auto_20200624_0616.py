# Generated by Django 3.0.6 on 2020-06-24 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_extenduser_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='firstname',
            new_name='firname',
        ),
    ]
