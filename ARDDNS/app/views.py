# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from app.models import *
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




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
		return HttpResponse("Create a new device")

	# Update device info
	if request.method == "PUT":
		return HttpResponse("Update device info")

	if request.method == "DELETE":
		return HttpResponse("Delete device")

