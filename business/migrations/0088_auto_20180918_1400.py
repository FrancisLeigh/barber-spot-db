# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0087_auto_20180918_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='daytradetime',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 14, 0, 42, 840265), null=True),
        ),
    ]