# Generated by Django 3.0.4 on 2020-03-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='num_ratings',
            field=models.FloatField(),
        ),
    ]
