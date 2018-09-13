# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import logging
from datetime import datetime, timedelta
from django.utils import timezone

class TimeSlot(models.Model):
  chair_id = models.ForeignKey('Chair', null=True)
  start = models.DateField(default=timezone.now)
  end = models.DateField()

  def __unicode__(self):
    return 'From: ' + str(self.start) + ' until: ' + str(self.end)

class Chair(models.Model):
  shop_id = models.ForeignKey('Shop', on_delete=models.SET_NULL, null=True)
  day_rate = models.IntegerField(default=100)

  def __unicode__(self):
    return 'Chair: ' + str(self.id) + ' | £' + str(self.day_rate) + ' | '

class Shop(models.Model):
  name = models.CharField(max_length=250)
  address = models.CharField(max_length=500)
  style = models.CharField(max_length=100)
  shop_image = models.CharField(max_length=1000)
  walk_ins = models.BooleanField(default=False)
  bookings = models.BooleanField(default=False)
  opening_time = models.TimeField(auto_now=False, default=datetime.now().replace(hour=9, minute=0, second=0, microsecond=0))
  closing_time = models.TimeField(auto_now=False, default=datetime.now().replace(hour=17, minute=30, second=0, microsecond=0))

  def __unicode__(self):
    return 'Shop: ' + str(self.id) + ' | ' + self.name

class Business(models.Model):
  name = models.CharField(max_length=250)
  address = models.CharField(max_length=500, blank=True)
  business_image = models.CharField(max_length=1000, blank=True)
  shops = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

  def __unicode__(self):
    return self.name
