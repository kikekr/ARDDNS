# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from app.models import Device, AuthenticationFailed
from app.util import build_api_key


import traceback





# VIEWS

# Home page
def display_home(request):

	template = 'index.html'
	context = {}
	return render_to_response(template, context,context_instance=RequestContext(request))



###########################################################################################


# API

#Permite Desactivar Seguridad csrf para hacer las peticiones ajax
@csrf_exempt
def devices(request):

	ip_address = request.META.get('REMOTE_ADDR')

	# Parseamos el contenido del cuerpo del mensaje
	data = json.loads(request.body)
		
	try:

		# Intentamos obtener los datos obligatorios para crear un dispositivo
		hostname = data["hostname"]
		mac_address = data["mac_address"]
		api_key = data["api_key"]

		# Comprobamos que el API KEY es válido
		if api_key == build_api_key(hostname, mac_address):

			# Si el API KEY es válido:

			# Create a new device
			if request.method == "POST":

				# Comprobamos si el dispositivo ya existe en base de datos
				try:
					device = Device.objects.get(hostname = hostname, mac_address = mac_address)

					# Si existe, no saltará la excepción, y por tanto indicamos que no se puede crear
					return HttpResponseBadRequest("Device already exists in database")

				# En caso de que no exista saltará la excepción 'DoesNotExist'
				except Device.DoesNotExist:

					# Almacenamos los datos del nuevo dispositivo en base de datos
					device = Device()
					device.hostname = hostname
					device.mac_address = mac_address
					device.ip = ip_address
				#	device.location = 
					device.last_seen = timezone.now()

					device.save()

					# TO DO: Actualizar servicio DNS

					return HttpResponse("Device created")

			# Update device info
			elif request.method == "PUT":

				# Comprobamos si el dispositivo ya existe en base de datos
				try:
					device = Device.objects.get(hostname = hostname, mac_address = mac_address)

					# Si existe, no saltará la excepción, actualizamos sus datos.

					device.hostname = hostname
					device.mac_address = mac_address
					device.ip = ip_address
					# device.location = 
					device.last_seen = timezone.now()

					device.save()

					# TO DO: Actualizar servicio DNS

					return HttpResponse('Device updated')

				# En caso de que no exista saltará la excepción 'DoesNotExist'
				except Device.DoesNotExist:

					return HttpResponseNotFound('Device not found')

		else:

			# Si el api key no es válido:
			# Almacenamos en base de datos el intento fallido de autenticación
			try:
				# Primero buscamos si ya exite algún registro fallido para esa ip
				authenticationFailed = AuthenticationFailed.objects.get(ip = ip_address)

			except AuthenticationFailed.DoesNotExist:

				# Si no existe, lo creamos
				authenticationFailed = AuthenticationFailed()
				authenticationFailed.ip = ip_address

				# Incrementamos el número de intentos fallidos de autenticació
			authenticationFailed.attemps = authenticationFailed.attemps + 1
			authenticationFailed.save()

			# TO DO: Al llegar a cierto número de intentos generar una alerta

			return HttpResponseBadRequest("Authentication error")

	except KeyError:

		# Si falta alguno de los datos obligatorios saltará la excepción 'KeyError'
		return HttpResponseBadRequest("Missing mandatory data")

