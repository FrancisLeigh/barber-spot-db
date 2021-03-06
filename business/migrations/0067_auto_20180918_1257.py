# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0066_auto_20180918_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayTradeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opens_at', models.TimeField(default=datetime.datetime(2018, 9, 18, 9, 0))),
                ('closes_at', models.TimeField(default=datetime.datetime(2018, 9, 18, 17, 30))),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TradeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.DayTradeTime')),
            ],
        ),
        migrations.AlterField(
            model_name='shop',
            name='hours',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TradeTime'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 12, 57, 39, 676147), null=True),
        ),
        migrations.DeleteModel(
            name='TradeTimes',
        ),
    ]
