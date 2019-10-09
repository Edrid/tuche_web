# Generated by Django 2.2.5 on 2019-10-09 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='intensity_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='intensity_y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='intensity_z',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='vehicle_type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
