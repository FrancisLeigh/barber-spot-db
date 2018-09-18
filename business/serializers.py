from rest_framework import serializers
from .models import Business, Shop, Chair, TimeSlot, TradeTime, DayTradeTime

import clr

class TimeSlotsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot
    ordering = ('chair_id', )
    fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
  class Meta:
    model = DayTradeTime

    fields = '__all__'

class HoursSerializer(serializers.ModelSerializer):
  monday = DaySerializer()
  tuesday = DaySerializer()
  wednesday = DaySerializer()
  tuesday = DaySerializer()
  thursday = DaySerializer()
  friday = DaySerializer()
  saturday = DaySerializer()
  sunday = DaySerializer()
  class Meta:
    model = TradeTime

    fields = '__all__'

class ChairsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chair
    exclude = ('time_slots', )

class ShopsSerializer(serializers.ModelSerializer):
  hours = HoursSerializer()
  class Meta:
    model = Shop
    exclude = ('chairs' ,)

class BusinessSerializer(serializers.ModelSerializer):
  shops = ShopsSerializer()
  class Meta:
    model = Business

    fields = '__all__'
