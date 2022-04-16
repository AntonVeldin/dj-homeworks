# Generated by Django 4.0.3 on 2022-03-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_created_at_measurement_sensor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
