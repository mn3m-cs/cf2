# Generated by Django 3.0 on 2020-09-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pod',
            name='pack_size',
            field=models.CharField(choices=[('1_dozen', '1 dozen (12)'), ('3_dozen', '3 dozen (36)'), ('5_dozen', '5 dozen (60)'), ('7_dozen', '7 dozen (84)')], max_length=64),
        ),
    ]
