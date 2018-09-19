# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.core import urlresolvers

from models import ShopDayTrade

import clr

from models import Business, Shop, Chair, TimeSlot, ShopDayTrade
DAYS= (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)
class ShopDayTradeAdminForm(forms.ModelForm):

  day = forms.MultipleChoiceField(choices=DAYS)

  class Meta:
    model = ShopDayTrade
    ordering = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    fields = '__all__'

  def clean_day(self):
    day = self.cleaned_data['day']
    if not day:
      raise forms.ValidationError("Pick a day")
    if len(day) > 1:
      day = ''.join(day)
      return day

    return day[0]

class ShopDayTradeAdmin(admin.ModelAdmin):
  form = ShopDayTradeAdminForm

admin.site.register(Business)
admin.site.register(Shop)
admin.site.register(Chair)
admin.site.register(TimeSlot)
admin.site.register(ShopDayTrade, ShopDayTradeAdmin)

