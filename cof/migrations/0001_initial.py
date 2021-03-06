# Generated by Django 3.0 on 2020-09-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('product_type', models.CharField(choices=[('large_machine', 'Coffee Machine Large'), ('small_machine', 'Coffee Machine Small'), ('espresso', 'Espresso Machine')], max_length=64)),
                ('water_line_compatible', models.BooleanField(blank=True)),
                ('model', models.CharField(choices=[('base_model', 'base model'), ('preimum_model', 'preimum model'), ('deluxe_model', 'deluxe model')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('product_type', models.CharField(choices=[('large_pod', 'Coffee Pod Large'), ('small_pod', 'Coffee Pod Small'), ('espresso', 'Espresso Pod')], max_length=64)),
                ('flavor', models.CharField(choices=[('vanilla', 'Vanilla'), ('caramel', 'Caramel'), ('psl', 'PSL'), ('mocha', 'Mocha'), ('hazelnut', 'Hazelnut')], max_length=64)),
                ('pack_size', models.CharField(choices=[('1_dozen', '1 dozen (12)'), ('3_dozen', '3 dozen (36)'), ('5_dozen', '3 dozen (60)'), ('7_dozen', '7 dozen (84)')], max_length=64)),
            ],
        ),
    ]
