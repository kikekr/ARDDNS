from django.db import models

import json

from app.util import build_api_key

# Create your models here.

class Device(models.Model):

	mac_address = models.CharField(max_length = 50, null = False, unique = True)
	hostname = models.CharField(max_length = 50, null = False)
	ip = models.CharField(max_length = 50, null = True, unique = True)
	last_seen = models.DateTimeField(null = True)
	location = models.CharField(max_length = 100, null = True)

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
		data["ip"] = self.ip
		# data["last_seen"] = self.last_seen
		data["location"] = self.location

		return json.dumps(data)

