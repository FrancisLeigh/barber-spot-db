# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 13:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0086_auto_20180918_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='hours',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TradeTime'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 13, 50, 36, 731660), null=True),
        ),
    ]
