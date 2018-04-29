# Generated by Django 2.0.4 on 2018-04-25 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20180424_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='actualEndDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='actualStartDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='addedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 25, 20, 52, 19, 216600), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='plannedEndDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='plannedStartDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='reportedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='revisedEndDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='revisedStartDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskallocate',
            name='assignedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskallocate',
            name='estimatedFinishDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskallocate',
            name='finisedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskallocate',
            name='startedOn',
            field=models.DateField(blank=True, null=True),
        ),
    ]