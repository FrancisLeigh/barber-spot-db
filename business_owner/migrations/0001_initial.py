# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('business_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_rate', models.IntegerField(default=100)),
                ('duration_weeks', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('style', models.CharField(max_length=100)),
                ('shop_image', models.CharField(max_length=1000)),
                ('walk_ins', models.BooleanField(default=False)),
                ('bookings', models.BooleanField(default=False)),
                ('chairs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business_owner.Chair')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='shops',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='business_owner.Shop'),
        ),
    ]