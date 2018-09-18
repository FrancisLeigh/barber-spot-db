from rest_framework import serializers
from .models import Business, Shop, Chair, TimeSlot

import clr

class TimeSlotsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot
    ordering = ('chair_id', )
    fields = '__all__'


class ChairsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chair
    exclude = ('time_slots', )

class ShopsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shop
    exclude = ('chairs' ,)

class BusinessSerializer(serializers.ModelSerializer):
  shops = ShopsSerializer()
  class Meta:
    model = Business

    fields = '__all__'
