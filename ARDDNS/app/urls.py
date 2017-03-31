from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.views import *


admin.autodiscover()

urlpatterns = patterns('',

                       # URL's de vistas

                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', 'app.views.display_home'),


                        #URL's de api
                        url(r'^devices/$', 'app.views.devices'),

)
