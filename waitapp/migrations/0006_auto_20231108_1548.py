# Generated by Django 3.2.21 on 2023-11-08 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('waitapp', '0005_auto_20231108_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truckdriver',
            name='check_in',
        ),
        migrations.AddField(
            model_name='truckdriver',
            name='check_in_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckdriver',
            name='check_in_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckdriver',
            name='finished_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='truckdriver',
            name='in_progress_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckdriver',
            name='finished_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckdriver',
            name='in_progress_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]