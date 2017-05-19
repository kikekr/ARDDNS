from django.contrib import admin

# Register your models here.

from app.models import *
# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    fields= ['mac_address','hostname', 'alive']

admin.site.register(Device,DeviceAdmin)

class AuthenticationFailedAdmin(admin.ModelAdmin):
    fields= ['ip','attemps']

admin.site.register(AuthenticationFailed,AuthenticationFailedAdmin)

class ConfigurationAdmin(admin.ModelAdmin):
    fields= ['num_attemps_to_alarm','dnszonefile']

admin.site.register(Configuration,ConfigurationAdmin)

class IpRegisterAdmin(admin.ModelAdmin):
    fields= ['ip_address','device', 'date']

admin.site.register(IpRegister,IpRegisterAdmin)

class LocationAdmin(admin.ModelAdmin):
    fields= ['country_code','country_name', 'region_code', 'region_name', 'city', 'zip_code', 'time_zone', 'latitude', 'longitude', 'metro_code']

admin.site.register(Location,LocationAdmin)