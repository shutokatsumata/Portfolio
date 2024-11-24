from django.contrib import admin
from .models import Genre, Category, Content

admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Content)