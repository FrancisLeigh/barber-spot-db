# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_auto_20180913_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='chairs',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Chair'),
        ),
    ]