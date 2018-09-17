from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  # /business/
  url(r'^$', views.BusinessView.as_view(), name='BusinessView'),

  # /business/shops/
  url(r'^shops/$', views.ShopsView.as_view(), name='shops'),

  # /business/shops/<shop_id>/
  url(r'^shops/(?P<shop_id>[0-9]+)/$', views.ShopView.as_view(), name='shop'),

  # /business/shops/<shop_id>/chairs
  url(r'^shops/(?P<shop_id>[0-9]+)/chairs/$', views.ChairsView.as_view(), name='shop_chairs'),

  # /business/shops/<shop_id>/chairs/<chair_id>
  url(r'^shops/(?P<shop_id>[0-9]+)/chairs/(?P<chair_id>[0-9]+)/$', views.ChairView.as_view(), name='shop_chair'),

  #/business/chairs/
  url(r'^chairs/$', views.ChairsView.as_view(), name='chairs'),

  #/business/chairs/<chair_id>
  url(r'^chairs/(?P<chair_id>[0-9]+)$', views.ChairView.as_view(), name='chair'),

  url(r'^chairs/(?P<chair_id>[0-9]+)/time-slots/$', views.TimeSlotsView.as_view(), name='chair-time-slots'),

  url(r'^time-slots/$', views.TimeSlotsView.as_view(), name='time_slots'),

  url(r'^time-slots/(?P<slot_id>[0-9]+)/$', views.TimeSlotView.as_view(), name='time_slot'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
