from rest_framework import serializers
from .models import Business, Shop, Chair, TimeSlot, ShopDayTrade

import clr
class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = '__all__'

class ShopsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shop
    fields = '__all__'

class ShopDayTradeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShopDayTrade
    fields = '__all__'

class ChairsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chair
    fields = '__all__'

class TimeSlotsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot
    ordering = ('chair_id', )
    fields = '__all__'
