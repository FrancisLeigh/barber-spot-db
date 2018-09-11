from rest_framework import serializers
from .models import Business, Shop, Chair

class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Business

    fields = '__all__'

class ShopsSerializer(serializers.ModelSerializer):
  chairs = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
    model = Shop

    fields = '__all__'

class ChairsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chair

    fields = '__all__'
