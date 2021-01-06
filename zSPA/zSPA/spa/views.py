from django.shortcuts import render


from spa.models import Images
# Create your views here.

def index(request, **kwargs):
	context = {}
	
	context = {
		'images': Images.objects.all()
	}

	return render(request, 'spa/main_SPA.html', context)


def grid_css(request, **kwargs):
    return render(request, 'spa/grid_css.html')


def form_example(request, **kwargs):
    return render(request, 'spa/form_example.html')
