from django.shortcuts import render
from decouple import config

from .models import Images


# Create your views here.

def index(request, **kwargs):
    """
    Render single page application and provide context data.
    :param request:
    :param kwargs:
    :return:
    """
    context = {
        'images': Images.objects.filter(is_active=True),
        'googleForm': config('googleForm', default=''),
        'googleMaps': config('googleMaps', default=''),
    }

    return render(request, 'spa/main_SPA.html', context)
