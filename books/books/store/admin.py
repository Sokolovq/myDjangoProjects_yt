from django.contrib import admin
from .models import Book, UserBookRelation


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['name', 'price', 'author_name']

@admin.register(UserBookRelation)
class AdminUserBookRelation(admin.ModelAdmin):
    pass
