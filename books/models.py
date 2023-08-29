# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from datetime import date, datetime, time
from django.utils import timezone

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_price_is_integer(value):
    if not isinstance(value, int):
        raise ValidationError(
            _('%(value)s is not an integer'),
            params={'value': value},
        )


class Book(models.Model):
    """
    Model representing a book in the book store.
    """
    book_store = models.CharField(max_length=100)  # Book store where the book is available
    book_title = models.CharField(max_length=100)  # Title of the book
    author_info = models.CharField(max_length=150)  # Information about the author(s)
    genre = models.CharField(max_length=50)  # Genre of the book
    isbn = models.CharField(max_length=13, unique=True)  # International Standard Book Number
    price = models.DecimalField(max_digits=5, decimal_places=2,
                                validators=[validate_price_is_integer])  # Price of the book
    count = models.PositiveIntegerField()  # Number of available copies
    date_publish = models.DateField(default=date.today)  # Date of publication

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        """
        Returns the absolute URL for accessing a detail view of the book.
        """
        return reverse('book-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['date_publish']

    def clean(self):
        cleaned_data = super().clean()
        current_time = timezone.now().time()
        if time(1, 0) <= current_time <= time(5, 0):
            raise ValidationError("Form cannot be submitted between 1 am and 5 am.")

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.startswith('9'):
            raise ValidationError("ISBN must start with '9'.")
        return isbn


class SaveHttpRequests(models.Model):
    request_method = models.CharField(max_length=6)
    request_path = models.CharField(max_length=150)
    request_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-request_datetime']
