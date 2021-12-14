

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin,
)


from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    login_url = 'account_login'
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(
    LoginRequiredMixin, 
    PermissionRequiredMixin, 
    DetailView
):
    model = Book
    login_url = 'account_login'
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status'

