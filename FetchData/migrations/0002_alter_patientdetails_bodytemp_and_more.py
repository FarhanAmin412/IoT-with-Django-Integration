# Generated by Django 4.0.2 on 2022-03-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FetchData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='BodyTemp',
            field=models.CharField(default='00.00', max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='Humidity',
            field=models.CharField(default='00.00', max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='RoomTemp',
            field=models.CharField(default='00.00', max_length=50),
        ),
    ]
