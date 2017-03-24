# -*- coding: utf-8 -*-
from django.shortcuts import render
from app.models import *
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse

# Create your views here.

# Vista Pagina de Inicio
#Vista de Configuración de Monolitos
# @login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin') or u.is_staff, login_url='/login/')
def display_home(request):

	template = 'index.html'
	context = {}
	return render_to_response(template, context,context_instance=RequestContext(request))
	#return HttpResponse("Hello world")

