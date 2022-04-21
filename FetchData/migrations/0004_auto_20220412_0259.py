# Generated by Django 3.2.9 on 2022-04-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FetchData', '0003_customerdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='OrderNum',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='Order',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]