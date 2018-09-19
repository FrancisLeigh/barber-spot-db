# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.core import urlresolvers

from models import ShopDayTrade

import clr

from models import Business, Shop, Chair, TimeSlot, ShopDayTrade
DAYS= (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
)
class ShopDayTradeAdminForm(forms.ModelForm):
  days = forms.MultipleChoiceField(choices = DAYS, required=False)
  class Meta:
    model = ShopDayTrade
    ordering = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    fields = '__all__'

  def clean_days(self):
    days = self.cleaned_data['days']
    print days
    print days
    if not days:
      raise forms.ValidationError("Pick a day or days")

    if len(days) > 1:
      days = ', '.join(days)
    else:
      days = ''.join(days)

    return days

class ShopDayTradeAdmin(admin.ModelAdmin):
  form = ShopDayTradeAdminForm

admin.site.register(Business)
admin.site.register(Shop)
admin.site.register(Chair)
admin.site.register(TimeSlot)
admin.site.register(ShopDayTrade, ShopDayTradeAdmin)

