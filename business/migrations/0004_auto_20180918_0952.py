# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 09:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20180918_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 9, 52, 59, 128811), null=True),
        ),
    ]