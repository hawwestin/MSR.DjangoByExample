from django.db import models
from django.utils import timezone

# Create your models here.


class Images(models.Model):
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=256)
	fileName = models.CharField(max_length=256)
	cssClass = models.CharField(max_length=256)

	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
