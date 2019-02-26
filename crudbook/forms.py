from django import forms
from .models import Book


class Settings:
    DATE_INPUT_FORMATS = [
        '%Y-%m-%d',  # '2006-10-25'
        '%Y.%m.%d',  # '2006-10-25'
        '%Y %m %d',  # '2006-10-25'
        '%d-%m-%Y',  # '25-10-2018'
        '%d.%m.%Y',  # '25-10-2018'
        '%d %m %Y',  # '25-10-2018'
        '%m/%d/%Y',  # '10/25/2006'
        '%m/%d/%y']  # '10/25/06'


class BookForm(forms.ModelForm):
    publication_date = forms.DateField(input_formats=Settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type',)
