from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Post

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Post)