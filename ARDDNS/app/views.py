# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from app.models import Device, AuthenticationFailed, Configuration, IpRegister, Location
from app.util import build_api_key, update_dns_zone
from app.ip_geolocation import requestGeoIp

import pandas as pd
import traceback





# VIEWS


# Home page
def display_home(request):

	template = 'index.html'
	context = {}

	devices = Device.objects.all()

	for device in devices:
		last_ip_register = IpRegister.objects.filter(device = device).order_by("-date").first()
		setattr(device, "last_ip_register", last_ip_register)

	context["devices"] = devices

	return render_to_response(template, context,context_instance=RequestContext(request))

# Create device
def create_device(request):
	pass

# Check devices
def check_all_devices(request):
	pass

# Device information
def info_device(request):
	pass

# Device details
def details_device(request, id_device):

	template = 'device_details.html'
	context = {}

	try:
		device = Device.objects.get(id = id_device)
		ip_registers = IpRegister.objects.filter(device = device).order_by("-date")
		setattr(device, "ip_registers", ip_registers)
		context["device"] = device
		return render_to_response(template, context,context_instance=RequestContext(request))
	except:
		return HttpResponseNotFound()

	

# Modify device
def modify_device(request):
	pass

# Login page
def custom_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            debug = login(request, user)
            url_param = request.GET.get('next', '/')
            return redirect(url_param)
    return render_to_response('login.html', context_instance=RequestContext(request))

# Logout page
def auth_logout(request):
    logout(request)
    return redirect('/')




###########################################################################################

def store_device_data(hostname, mac_address, ip_address):

	# Almacenamos los datos del nuevo dispositivo en base de datos
	device = Device()
	device.hostname = hostname
	device.mac_address = mac_address

	device.save()

	ipRegister = IpRegister()
	ipRegister.ip_address = ip_address
	ipRegister.date = timezone.now()
	ipRegister.device = device

	try:
		json_ipinfo = requestGeoIp(ip_address)

		print(json_ipinfo)
		
		location = Location()
		location.country_code = json_ipinfo["country_code"]
		location.country_name = json_ipinfo["country_code"]
		location.region_code = json_ipinfo["country_code"]
		location.region_name = json_ipinfo["country_code"]
		location.city = json_ipinfo["country_code"]

		try:
			location.zip_code = int(json_ipinfo["country_code"])
		except:
			location.zip_code = None

		location.time_zone = json_ipinfo["country_code"]
		
		try:
			location.latitude = float(json_ipinfo["country_code"])
		except:
			location.latitude = None

		try:	
			location.longitude = float(json_ipinfo["country_code"])
		except:
			location.longitude = None

		try:
			location.metro_code = int(json_ipinfo["country_code"])
		except:
			location.metro_code = None

		location.save()
		print(location)
		ipRegister.location = location
	
	except:
		print(traceback.print_exc())

	ipRegister.save()



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
		if True:
		# if api_key == build_api_key(hostname, mac_address):

			# Si el API KEY es válido:

			dnszonefile = Configuration.objects.get(id = 1).dnszonefile

			# Create a new device
			if request.method == "POST":

				# Comprobamos si el dispositivo ya existe en base de datos
				try:
					device = Device.objects.get(hostname = hostname, mac_address = mac_address)

					# Si existe, no saltará la excepción, y por tanto indicamos que no se puede crear
					return HttpResponseBadRequest("Device already exists in database")

				# En caso de que no exista saltará la excepción 'DoesNotExist'
				except Device.DoesNotExist:

					try:
						store_device_data(hostname, mac_address, ip_address)
					except:
						print(traceback.print_exc())

						# TO DO: Return HttpBadRequest
						return HttpResponse("IP is already in use")

					# Actualizamos el servicio DNS
					update_dns_zone(dnszonefile, hostname, ip_address)

					return HttpResponse("Device created")

			# Update device info
			elif request.method == "PUT":

				# Comprobamos si el dispositivo ya existe en base de datos
				try:
					device = Device.objects.get(hostname = hostname, mac_address = mac_address)

					# Si existe, no saltará la excepción, actualizamos sus datos.

					try:
						store_device_data(hostname, mac_address, ip_address)
					except:
						# TO DO: Return HttpBadRequest
						return HttpResponse("IP is already in use")

					# Actualizamos el servicio DNS
					update_dns_zone(dnszonefile, hostname, ip_address)

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

