from django.shortcuts import render


# Create your views here.

def index(request, **kwargs):
    return render(request, 'spa/main_SPA.html')
