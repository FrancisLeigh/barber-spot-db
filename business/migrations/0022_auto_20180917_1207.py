# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0021_auto_20180917_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]