# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

from models import Shop

import logging

def index(request):
  all_shops = Shop.objects.all()
  shops = []

  for shop in all_shops:
    shops.append({
      'name': shop.name,
      'address': shop.address,
      'style': shop.style,
      'shop_image': shop.shop_image,
      'walk_ins': shop.walk_ins,
      'bookings': shop.bookings
    })

  return JsonResponse({
    'data': shops
  })

def shop(request, shop_id):
  filtered_shop = Shop.objects.filter(id=shop_id)

  logging.warn(filtered_shop.values())
  shop = {}
  for s in filtered_shop:
    shop['name'] = s.name
    shop['address'] = s.address
    shop['style'] = s.style
    shop['shop_image'] = s.shop_image
    shop['walk_ins'] = s.walk_ins
    shop['bookings'] = s.bookings

  return JsonResponse(shop)

# def chairs(request, shop_id):
#   shop_chairs = Shop.objects.filter(id=shop_id).values('chairs')

#   chairs = []
#   return JsonResponse({ 'data': chairs })
