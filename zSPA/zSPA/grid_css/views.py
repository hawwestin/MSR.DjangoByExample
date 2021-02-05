from django.shortcuts import render

# Create your views here.


def grid_css(request, **kwargs):
    return render(request, 'grid_css/grid_css.html')
