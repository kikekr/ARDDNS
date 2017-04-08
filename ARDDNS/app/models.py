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
		# data["last_seen"] = self.last_seen

		return json.dumps(data)


class IpRegister(models.Model):


	device = models.ForeignKey('Device')
	ip_address = models.CharField(max_length = 50, null = False)
	location = models.CharField(max_length = 100, null = True)
	date = models.DateTimeField(null = False)

	def __str__(self):
		return str(self.device) + " - " + str(self.ip_address) + " at " + str(self.date)

	class Meta:
		unique_together = (
			('ip_address', 'device')
		)


class AuthenticationFailed(models.Model):

	ip = models.CharField(max_length = 50, null = False, unique = True)
	attemps = models.IntegerField(null = False, default = 0)

	def __str__(self):
		return str(self.ip) + ": " + str(self.attemps) + " attemps failed"

