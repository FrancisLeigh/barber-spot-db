# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0028_shop_business_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='business_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Business'),
        ),
    ]