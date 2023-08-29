# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Book, SaveHttpRequests
from .forms import BookForm
from .my_logg import *

setup_logging()
logger = logging.getLogger('books_app')


class BookListView(ListView):
    """
    Display a list of books.
    """
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
    paginate_by = 10


class BookDetailView(DetailView):
    """
    Display the details of the selected book.
    """
    model = Book


class BookCreateView(CreateView, ListView):
    """
    Display created book form.
    """
    model = Book
    form_class = BookForm
    template_name = 'books/add_book.html'
    context_object_name = 'books'
    paginate_by = 10

    def form_valid(self, form):
        logger.info('Created new book with title: {}'.format(form.cleaned_data['book_title']))
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    """
    Display update selected book form.
    """
    model = Book
    fields = ['book_store', 'book_title', 'author_info', 'genre', 'isbn', 'price']

    def form_valid(self, form):
        logger.info('Updated book with title: {}'.format(form.cleaned_data['book_title']))
        return super().form_valid(form)


class RequestListView(ListView):
    """
    Display a list of last 10 requests.
    """
    model = SaveHttpRequests
    template_name = 'books/saved_requests.html'
    context_object_name = 'requests'
    queryset = SaveHttpRequests.objects.order_by('-id')[:10]

