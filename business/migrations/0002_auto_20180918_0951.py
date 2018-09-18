# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 09:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=datetime.datetime(2018, 9, 25, 9, 51, 41, 560572), null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='chair',
            name='duration_weeks',
        ),
        migrations.AddField(
            model_name='chair',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
        migrations.AddField(
            model_name='shop',
            name='business_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Business'),
        ),
        migrations.AddField(
            model_name='shop',
            name='closing_time',
            field=models.TimeField(default=datetime.datetime(2018, 9, 18, 17, 30)),
        ),
        migrations.AddField(
            model_name='shop',
            name='opening_time',
            field=models.TimeField(default=datetime.datetime(2018, 9, 18, 9, 0)),
        ),
        migrations.AlterField(
            model_name='business',
            name='shops',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='chairs',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Chair'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='chair_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Chair'),
        ),
        migrations.AddField(
            model_name='chair',
            name='time_slots',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TimeSlot'),
        ),
    ]
