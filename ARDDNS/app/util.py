# -*- coding: utf-8 -*-
import hashlib





def build_api_key(hostname, mac_address):

	####################################################################

	# buid_api_key

	# Función que calcula el API key en función de un hostname y una di-
	# rección MAC utilizando el hash MD5.

	# Parámetros:

	#	- hostname:	Nombre de dispositivo
	#	- mac_address: Dirección MAC del dispositivo

	# Salidas:

	#	- Código md5 de la combinación de los strings hostname y mac


	####################################################################

	return hashlib.md5(str(hostname) + "" + str(mac_address)).hexdigest()