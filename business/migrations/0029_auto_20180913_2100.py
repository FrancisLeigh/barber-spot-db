# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0028_auto_20180913_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradinghours',
            name='shop_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
    ]