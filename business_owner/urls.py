from django.conf.urls import url
from . import views

urlpatterns = [
  # /business-owner/
  url(r'^$', views.index, name='index'),

  # /business-owner/shops/
  url('shops/', views.shops, name='shops'),

  # /business-owner/shops/2/
  url(r'^shops/(?P<shop_id>[0-9]+)/$', views.shop, name='shop'),

  #/shops/2/chairs
  # url(r'^(?P<shop_id>[0-9]+)/chairs/', views.chairs, name='chairs')
]
