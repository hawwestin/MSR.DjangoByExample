from django.shortcuts import render

# Create your views here.

def form_example(request, **kwargs):
    return render(request, 'form_example/form_example.html')
