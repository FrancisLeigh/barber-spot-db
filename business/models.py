# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import logging
import clr
from datetime import datetime, timedelta
from django.utils import timezone
from address.models import AddressField

class TimeSlot(models.Model):
  chair_id = models.ForeignKey('Chair', null=True)
  start_date = models.DateField(default=timezone.now)
  end_date = models.DateField(default=datetime.now()+timedelta(days=7), null=True)

  def __unicode__(self):
    return 'From: ' + str(self.start_date) + ' until: ' + str(self.end_date)

class Chair(models.Model):
  shop_id = models.ForeignKey('Shop', null=True)
  day_rate = models.IntegerField(default=100)
  time_slots = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, null=True, editable=False, blank=True)

  def __unicode__(self):
    return 'Chair: ' + str(self.id) + ' | £' + str(self.day_rate) + 'pd'

class Shop(models.Model):
  business_id = models.ForeignKey('Business', null=True)
  name = models.CharField(max_length=250)
  address = AddressField(null=True)
  style = models.CharField(max_length=100)
  shop_image = models.CharField(max_length=1000)
  walk_ins = models.BooleanField(default=False)
  bookings = models.BooleanField(default=False)
  chairs = models.ForeignKey('Chair', null=True, on_delete=models.CASCADE, blank=True, editable=False)

  hours = models.OneToOneField('TradeTime', null=True)

  def __unicode__(self):
    return 'Shop: ' + str(self.id) + ' | ' + self.name

class TradeTime(models.Model):
  shop_id = models.OneToOneField('Shop', null=True)
  monday = models.ForeignKey('DayTradeTime', related_name='monday', null=True, blank=True)
  tuesday = models.ForeignKey('DayTradeTime', related_name='tuesday', null=True, blank=True)
  wednesday = models.ForeignKey('DayTradeTime', related_name='wednesday', null=True, blank=True)
  thursday = models.ForeignKey('DayTradeTime', related_name='thursday', null=True, blank=True)
  friday = models.ForeignKey('DayTradeTime', related_name='friday', null=True, blank=True)
  saturday = models.ForeignKey('DayTradeTime', related_name='saturday', null=True, blank=True)
  sunday = models.ForeignKey('DayTradeTime', related_name='sunday', null=True, blank=True)

  def __unicode__(self):
    return str(self.shop_id)

class DayTradeTime(models.Model):
  shop_id = models.ForeignKey('Shop', null=True)
  opens_at = models.TimeField(auto_now=False, default=datetime.now().replace(hour=9, minute=0, second=0, microsecond=0))
  closes_at = models.TimeField(auto_now=False, default=datetime.now().replace(hour=17, minute=30, second=0, microsecond=0))
  closed = models.BooleanField(default=False)

  def __unicode__(self):
    if self.closed:
      return 'closed'
    else:
      return str(self.opens_at) + ' - ' + str(self.closes_at)
class Business(models.Model):
  name = models.CharField(max_length=250)
  address = AddressField(null=True)
  business_image = models.CharField(max_length=1000, blank=True)
  shops = models.ForeignKey(Shop, null=True, editable=False)

  def __unicode__(self):
    return self.name + ' | ' + str(self.address)
