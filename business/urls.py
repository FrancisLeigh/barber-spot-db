from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  # /business/
  url(r'^$', views.BusinessView.as_view(), name='business'),
  url(r'^address/$', views.AddressView.as_view(), name='business_address'),

  # /business/shops/
  url(r'^shops/$', views.ShopsView.as_view(), name='shops'),
  # /business/shops/<shop_id>/
  url(r'^shops/(?P<shop_id>[0-9]+)/$', views.ShopView.as_view(), name='shop'),
  url(r'^shops/(?P<shop_id>[0-9]+)/address/$', views.AddressView.as_view(), name='shop_address'),
  # /business/shops/<shop_id>/chairs
  url(r'^shops/(?P<shop_id>[0-9]+)/chairs/$', views.ChairsView.as_view(), name='shop_chairs'),
  # /business/shops/<shop_id>/chairs/<chair_id>
  url(r'^shops/(?P<shop_id>[0-9]+)/chairs/(?P<chair_id>[0-9]+)/$', views.ChairView.as_view(), name='shop_chair'),

  url(r'^hours/(?P<shop_id>[0-9]+)/$', views.TradingHoursView.as_view(), name='shop-hours'),
  url(r'^hours/(?P<shop_id>[0-9]+)/(?P<day_id>[0-9]+)/$', views.TradingHourView.as_view(), name='shop-hour'),

  #/business/chairs/
  url(r'^chairs/$', views.ChairsView.as_view(), name='chairs'),
  #/business/chairs/<chair_id>
  url(r'^chairs/(?P<chair_id>[0-9]+)$', views.ChairView.as_view(), name='chair'),

  url(r'^time-slots/(?P<chair_id>[0-9]+)/$', views.TimeSlotsView.as_view(), name='chair_time-slots'),
  url(r'^time-slots/(?P<chair_id>[0-9]+)/(?P<slot_id>[0-9]+)/$', views.TimeSlotView.as_view(), name='time_slot'),
]
