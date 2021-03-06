# Generated by Django 2.0.4 on 2018-04-21 12:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_auto_20180421_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskStatus',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='actualEndDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='actualStartDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='addedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_addedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='addedOn',
            field=models.DateField(default=datetime.datetime(2018, 4, 21, 17, 48, 3, 618784)),
        ),
        migrations.AddField(
            model_name='task',
            name='estimatedHours',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='task',
            name='plannedEndDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='plannedStartDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'High'), ('LOW', 'Low'), ('TRI', 'Trivial')], default='LOW', max_length=5),
        ),
        migrations.AddField(
            model_name='task',
            name='releaseNote',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='releasedDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='reportedOn',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='revisedEndDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='revisedStartDate',
            field=models.DateField(blank=True, default=datetime.date(2018, 4, 21), null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.taskStatus'),
        ),
    ]
