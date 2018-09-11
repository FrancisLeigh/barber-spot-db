from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  # /business-owner/
  url(r'^$', views.BusinessView.as_view(), name='BusinessView'),

  # /business-owner/shops/
  url(r'^shops/$', views.ShopsView.as_view(), name='shops'),

  # /business-owner/shops/2/
  url(r'^shops/(?P<shop_id>[0-9]+)/$', views.ShopView.as_view(), name='shop'),

  url(r'^chairs/$', views.ChairsView.as_view(), name='chairs'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
