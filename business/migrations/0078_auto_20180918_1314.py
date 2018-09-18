# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 13:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0077_auto_20180918_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 13, 14, 5, 229003), null=True),
        ),
        migrations.AlterField(
            model_name='tradetime',
            name='wednesday',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='business.DayTradeTime'),
        ),
    ]
