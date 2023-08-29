# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory
from .models import Book
from django.forms.widgets import SelectDateWidget


class BookForm(ModelForm):
    """
    Form for editing book information based on the Book model.
    """

    class Meta:
        model = Book
        fields = ['book_store', 'book_title', 'genre', 'isbn', 'price', 'count', 'date_publish']
        labels = {
            'book_store': _('Book store'),
            'book_title': _('Book title'),
            'author_info': _('Book authors'),
            'genre': _('Book genre'),
            'isbn': _('International standard book number'),
            'price': _('Book price'),
            'count': _('Number of copies available'),
            'date_publish': _('Book publish date'),
        }
        widgets = {
            'date_publish': SelectDateWidget(empty_label="Choose date", years=range(1950, 2051))
        }
