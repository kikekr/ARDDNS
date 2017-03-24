from django.db import models

# Create your models here.

class Device(models.Model):

	mac_address = models.CharField(max_length = 50, null = False, unique = True)
	hostname = models.CharField(max_length = 50, null = False)
	ip = models.CharField(max_length = 50, null = True, unique = True)
	last_seen = models.DateTimeField(null = True)
	location = models.CharField(max_length = 100, null = True)

