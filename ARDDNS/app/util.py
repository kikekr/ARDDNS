# -*- coding: utf-8 -*-

import hashlib

def build_api_key(hostname, mac_address):

	####################################################################

	# buid_api_key

	# Función que calcula el API key en función de un hostname y una di-
	# rección MAC utilizando el hash MD5.

	# Parámetros:

	#	- hostname:		Nombre de dispositivo
	#	- mac_address: 	Dirección MAC del dispositivo

	# Salidas:

	#	- Código md5 de la combinación de los strings hostname y mac


	####################################################################

	return hashlib.md5(str(hostname) + "" + str(mac_address)).hexdigest()



def update_dns_zone(dnszonefile, hostname, ip_address):

	####################################################################

	# update_dns_zone

	# Función que actualiza el fichero de zona del servicio DNS

	# Parámetros:

	#	- dnszonefile:	Ruta del fichero de zona
	#	- hostname: 	Nombre del dispositivo
	#	- ip_address:	Dirección IP del dispositivo

	####################################################################

	# Definimos la nueva línea del fichero de zona
	newline = str(hostname) + "	IN	A		" + str(ip_address)

	# Abrimos el fichero de zona
	f = open(dnszonefile, "r+")

	# Comprobamos si ya hay algún registro para ese hostname
	for line in f:
		if hostname in line:
			# Si lo hay lo reemplazamos y salimos de la función
			line = "ubuntu	IN	A		" + str(ip_address) + "\n"
			return

	# Si no lo hay lo añadimos al final
	f.writelines(str(hostname) + "	IN	A		" + str(ip_address) + "\n")

	f.close()