# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0014_auto_20180913_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='chairs',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='business.Chair'),
        ),
    ]