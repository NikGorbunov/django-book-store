from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDetailView, RequestListView

urlpatterns = [
    path('', BookListView.as_view(), name='books-home'),
    path('add_book/', BookCreateView.as_view(), name='books-add-book'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('saved_requests/', RequestListView.as_view(), name='saved-requests')
]