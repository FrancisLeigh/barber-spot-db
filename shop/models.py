# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import logging

class Chair(models.Model):
  day_rate = models.IntegerField(default=100)
  duration_weeks = models.IntegerField(default=1)

  def __unicode__(self):
    return '£' + str(self.day_rate) + ' for ' + str(self.duration_weeks) + ' week(s)'


# Red pk/id 1
class Shop(models.Model):
  name = models.CharField(max_length=250)
  address = models.CharField(max_length=500)
  style = models.CharField(max_length=100)
  shop_image = models.CharField(max_length=1000)
  chairs = models.ForeignKey(Chair, on_delete=models.SET_NULL, blank=True, null=True)
  walk_ins = models.BooleanField(default=False)
  bookings = models.BooleanField(default=False)

  def __unicode__(self):
    return 'Shop: ' + self.name
