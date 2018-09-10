from django.conf.urls import url
from . import views


urlpatterns = [
  # /shops/
  url(r'^$', views.index, name='index'),

  # /shops/2/
  url(r'^(?P<shop_id>[0-9]+)/$', views.shop, name='shop'),

  #/shops/2/chairs
  # url(r'^(?P<shop_id>[0-9]+)/chairs/', views.chairs, name='chairs')
]
