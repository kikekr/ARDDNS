# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from app.models import Device
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

	# Create a new device
	if request.method == "POST":

		# Parseamos el contenido del cuerpo del mensaje
		data = json.loads(request.body)
		
		try:

			# Intentamos obtener los datos obligatorios para crear un dispositivo
			hostname = data["hostname"]
			mac_address = data["mac_address"]
			api_key = data["api_key"]

		#	print(build_api_key(hostname, mac_address))

			# Comprobamos que el API KEY es válido
			if api_key == build_api_key(hostname, mac_address):

				# Si el API KEY es válido:

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
					device.ip = request.META.get('REMOTE_ADDR')
				#	device.location = 
					device.last_seen = timezone.now()

					device.save()


					#TO DO: Return HTTP 201 CREATED
					return HttpResponse("Device created")

			else:
				# Si el api key no es válido:

				# TO DO: Incrementar contador de intentos
				# Al llegar a cierto número de intentos generar una alerta

				return HttpResponseBadRequest("Authentication error")

		except KeyError:
			# Si falta alguno de los datos obligatorios saltará la excepción 'KeyError'
			return HttpResponseBadRequest("Missing mandatory data")


	# Update device info
	if request.method == "PUT":
		return HttpResponse("Update device info")

	if request.method == "DELETE":
		return HttpResponse("Delete device")

