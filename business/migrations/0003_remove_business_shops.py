# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20180917_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='shops',
        ),
    ]