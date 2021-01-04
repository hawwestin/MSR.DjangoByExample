from django.shortcuts import render


# Create your views here.

def index(request, **kwargs):
    return render(request, 'spa/main_SPA.html')


def grid_css(request, **kwargs):
    return render(request, 'spa/grid_css.html')

def form_example(request, **kwargs):
	return render(request, 'spa/form_example.html')
	