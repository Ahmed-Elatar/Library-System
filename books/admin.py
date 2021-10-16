from django.contrib import admin

# Register your models here.
from books.models import books

admin.site.register(books)
