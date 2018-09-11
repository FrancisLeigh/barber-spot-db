from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from business import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^business/', include('business.urls')),
]


urlpatterns = format_suffix_patterns(urlpatterns)
