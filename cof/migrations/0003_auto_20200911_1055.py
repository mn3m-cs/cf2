# Generated by Django 3.0 on 2020-09-11 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0002_auto_20200910_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='water_line_compatible',
            new_name='water_line_compitable',
        ),
    ]
