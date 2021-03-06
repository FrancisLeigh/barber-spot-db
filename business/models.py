# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import logging
import clr
from datetime import datetime, timedelta
from django.utils import timezone
from address.models import AddressField

class Business(models.Model):
  name = models.CharField(max_length=250)
  address = AddressField(null=True)
  business_image = models.CharField(max_length=1000, blank=True)

  def __unicode__(self):
    return self.name + ' | ' + str(self.address)

class Shop(models.Model):
  business_id = models.ForeignKey('Business', null=True)
  name = models.CharField(max_length=250)
  address = AddressField(null=True)
  style = models.CharField(max_length=100)
  shop_image = models.CharField(max_length=1000)
  walk_ins = models.BooleanField(default=False)
  bookings = models.BooleanField(default=False)
  closed_on_public_holidays = models.BooleanField(default=True, blank=True)

  def __unicode__(self):
    return 'Shop: ' + str(self.id) + ' | ' + self.name

class ShopDayTrade(models.Model):
  shop_id = models.ForeignKey('Shop', null=True)
  day = models.CharField(max_length=100, blank=True)
  opens = models.TimeField(auto_now=False, default=datetime.now().replace(hour=9, minute=0, second=0, microsecond=0))
  closes = models.TimeField(auto_now=False, default=datetime.now().replace(hour=17, minute=30, second=0, microsecond=0))
  closed = models.BooleanField(default=False)

  def __unicode__(self):
    if self.closed is True:
      return self.day + ' | closed'
    else:
      return self.day + ' | ' + str(self.opens) + ' - ' + str(self.closes)

class Chair(models.Model):
  shop_id = models.ForeignKey('Shop', null=True)
  day_rate = models.IntegerField(default=100)

  def __unicode__(self):
    return 'Chair: ' + str(self.id) + ' | £' + str(self.day_rate) + 'pd'

class TimeSlot(models.Model):
  chair_id = models.ForeignKey('Chair', null=True)
  start_date = models.DateField(default=timezone.now)
  end_date = models.DateField(default=datetime.now()+timedelta(days=7), null=True)

  def __unicode__(self):
    return 'From: ' + str(self.start_date) + ' until: ' + str(self.end_date)
