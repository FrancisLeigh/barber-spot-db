# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core import urlresolvers

from models import Business, Shop, Chair, TimeSlot, TradeTime, DayTradeTime

admin.site.register(Business)
admin.site.register(Shop)
admin.site.register(Chair)
admin.site.register(TimeSlot)
admin.site.register(TradeTime)
admin.site.register(DayTradeTime)

