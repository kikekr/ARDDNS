from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.views import *


admin.autodiscover()

urlpatterns = patterns('',

                       # URL's de vistas

                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', 'app.views.display_home', name='show-devices'),
                        url(r'^login/$', 'app.views.custom_login', name='login'),
                        url(r'^auth_logout/$', 'app.views.auth_logout', name='auth_logout'),

                        url(r'^devices/create/$', 'app.views.create_device', name='create-device'),
                        url(r'^devices/check/$', 'app.views.create_device', name='check-all-devices'),
                        url(r'^devices/info/(?P<id_device>\d+)$', 'app.views.info_device', name='info-device'),
    					url(r'^devices/details/(?P<id_device>\d+)$', 'app.views.details_device', name='details-device'),
					    url(r'^device/modify/(?P<id_device>\d+)$', 'app.views.modify_device', name='modify-device'),

					    url(r'^location/show/(?P<id_location>\d+)$', 'app.views.show_location', name='show-location'),


                        #URL's de api
                        url(r'^devices/$', 'app.views.devices'),

)
