from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Book
from .forms import BookForm


def index(request):
    return redirect('crudbook:book_list')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'crudbook/book_list.html', {'books': books})


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('crudbook/includes/partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string('crudbook/includes/partial_book_create.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)
