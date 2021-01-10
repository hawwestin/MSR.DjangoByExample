from django.db import models
from django.utils import timezone

# Create your models here.


class Images(models.Model):
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=256)
	image = models.ImageField(upload_to='spa/', null=True, blank=True)
	fileName = models.CharField(max_length=256, null=True, blank=True)
	cssClass = models.CharField(max_length=256, null=True, blank=True)
	# todo take sth to adjust order of pictures on site. 

	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
