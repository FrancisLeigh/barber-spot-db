# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 11:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0038_auto_20180918_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openclosetimes',
            name='day_name',
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 11, 51, 31, 45273), null=True),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='friday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='F', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='monday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='M', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='saturday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SA', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Shop'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='sunday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SU', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='thursday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TH', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='tuesday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TU', to='business.OpenCloseTimes'),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='wednesday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='W', to='business.OpenCloseTimes'),
        ),
    ]
