# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 11:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0025_auto_20180918_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 11, 34, 55, 95116), null=True),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='friday',
            field=models.ForeignKey(db_column='friday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='F', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='monday',
            field=models.ForeignKey(db_column='monday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='M', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='saturday',
            field=models.ForeignKey(db_column='saturday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SA', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='sunday',
            field=models.ForeignKey(db_column='sunday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SU', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='thursday',
            field=models.ForeignKey(db_column='thursday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TH', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='tuesday',
            field=models.ForeignKey(db_column='tuesday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TU', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='wednesday',
            field=models.ForeignKey(db_column='wednesday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='W', to='business.OpenCloseTimes'),
        ),
    ]
