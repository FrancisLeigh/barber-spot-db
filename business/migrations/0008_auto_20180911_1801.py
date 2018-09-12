# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_auto_20180911_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='chair',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
        migrations.AddField(
            model_name='shop',
            name='business_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Business'),
        ),
    ]
