# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 10:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0015_auto_20180918_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 10, 37, 56, 577101), null=True),
        ),
    ]
