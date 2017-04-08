# -*- coding: utf-8 -*-

from django.db import models
from app.util import build_api_key
import json

# Create your models here.


class Configuration(models.Model):

	num_attemps_to_alarm = models.IntegerField(null = False, default = 3)
	domain = models.CharField(max_length = 50, help_text = "Nombre del dominio", null = False	)
	dnszonefile = models.CharField(max_length = 100, help_text = "Ubicación del fichero de zona DNS", null = False)

	def __str__(self):
		return "Configuration"

class Device(models.Model):

	mac_address = models.CharField(max_length = 50, null = False, unique = True)
	hostname = models.CharField(max_length = 50, null = False)
	alive = models.BooleanField(null = False, default = False)

	def __str__(self):
		return self.hostname

	def get_api_key(self):

		####################################################################

		# Función que devuelve el api key del dispositivo, delegando en la 
		# función 'build_api_key' del módulo app.util

		# Entradas:

		# Salidas:
		#	- Información del dispositivo en formato JSON.

		####################################################################

		return build_api_key(self.hostname, self.mac_address)
		

	def to_json(self):

		####################################################################

		# Función que convierte la información del dispositivo a formato
		# JSON.

		# Entradas:

		# Salidas:
		#	- Información del dispositivo en formato JSON.

		####################################################################

		data = {}
		data["mac_address"] = self.mac_address
		data["hostname"] = self.hostname
		data["alive"] = self.last_seen

		return json.dumps(data)


class IpRegister(models.Model):


	device = models.ForeignKey('Device')
	ip_address = models.CharField(max_length = 50, null = False)
	location = models.ForeignKey('Location', null = True)
	date = models.DateTimeField(null = False)

	def __str__(self):
		if self.location != None:
			return str(self.device) + " - " + str(self.ip_address) + " ( " + str(self.location.country_code) + ") at " + str(self.date)
		else:
			return str(self.device) + " - " + str(self.ip_address) + " at " + str(self.date)

	class Meta:
		unique_together = (
			('ip_address', 'device')
		)

class Location(models.Model):

	country_code = models.CharField(max_length = 5, null = True)
	country_name = models.CharField(max_length = 50, null = True)
	region_code = models.CharField(max_length = 50, null = True)	
	region_name = models.CharField(max_length = 50, null = True)
	city = models.CharField(max_length = 50, null = True)
	zip_code = models.IntegerField(null = True)
	time_zone = models.CharField(max_length = 50, null = True)
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)
	metro_code = models.IntegerField(null = True)

	def __str__(self):
		if ((self.city != None) and (self.region_name != None) and (self.country_name != None)):
			return str(self.city) + " - " + str(self.region_name) + " (" + str(self.country_name) + ")"
		else:
			return None


class AuthenticationFailed(models.Model):

	ip = models.CharField(max_length = 50, null = False, unique = True)
	attemps = models.IntegerField(null = False, default = 0)

	def __str__(self):
		return str(self.ip) + ": " + str(self.attemps) + " attemps failed"

