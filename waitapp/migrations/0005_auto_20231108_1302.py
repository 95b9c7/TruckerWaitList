# Generated by Django 3.2.21 on 2023-11-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitapp', '0004_auto_20231106_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckdriver',
            name='check_in_employee',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='truckdriver',
            name='finished_employee',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='truckdriver',
            name='in_progress_employee',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
