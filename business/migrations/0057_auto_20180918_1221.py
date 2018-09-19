# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 12:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0056_auto_20180918_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 12, 21, 21, 584455), null=True),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='friday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='F', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='monday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='M', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='saturday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SA', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='sunday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SU', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='thursday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TH', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='tuesday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TU', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtime',
            name='wednesday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='W', to='business.OpenCloseTimes'),
        ),
    ]