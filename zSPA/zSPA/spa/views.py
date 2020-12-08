from django.shortcuts import render


# Create your views here.

def index(request, **kwargs):
    return render(request, 'spa/main_SPA.html')


def grid_css(request, **kwargs):
    return render(request, 'spa/grid_css.html')
