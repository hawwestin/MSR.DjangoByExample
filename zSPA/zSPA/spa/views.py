from django.shortcuts import render


from .models import Images
# Create your views here.

def index(request, **kwargs):
	context = {}
	
	context = {
		'images': Images.objects.all()
	}

	return render(request, 'spa/main_SPA.html', context)




