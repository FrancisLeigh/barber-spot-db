# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0032_auto_20180913_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='chair_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Chair'),
        ),
    ]