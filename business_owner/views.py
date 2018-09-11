# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Business, Shop, Chair
from .serializers import BusinessSerializer, ShopsSerializer, ChairsSerializer

import logging

# multiples views

class ShopsView(APIView):

  def get(self, request):
    ss = Shop.objects.all()
    serializer = ShopsSerializer(ss, many=True)

    return Response(serializer.data)

class ChairsView(APIView):

  def get(self, request):
    cs = Chair.objects.all()
    serializer = ChairsSerializer(cs, many=True)

    return Response(serializer.data)

# singleton views
class BusinessView(APIView):

  def get(self, request):
    b = Business.objects.all()
    serializer = BusinessSerializer(b, many=True)

    return Response(serializer.data)

class ShopView(APIView):

  def get(self, request, shop_id):
    s = Shop.objects.filter(id=shop_id)
    serializer = ShopsSerializer(s, many=True)

    return Response(serializer.data)

