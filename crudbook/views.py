from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'crudbook/book_list.html', {'books': books})
