from django.shortcuts import render
from decouple import config


from .models import Images
# Create your views here.

def index(request, **kwargs):
	context = {}
	
	context = {
		'images': Images.objects.filter(is_active=True),
		'googleForm': config('googleForm'),
		'googleMaps': config('googleMaps'),
	}

	return render(request, 'spa/main_SPA.html', context)




