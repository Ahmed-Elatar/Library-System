from django.urls import path
from books.views import bookspage

urlpatterns = [
    path('', bookspage,name="Bookspage"),
]
