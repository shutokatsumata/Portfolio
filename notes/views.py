from django.shortcuts import render, get_object_or_404
from .models import Genre, Category, Content

# ジャンル一覧
def genre_list(request):
    genres = Genre.objects.all()

    return render(request, 'notes/genre_list.html', {'genres': genres})

# カテゴリ一覧
def category_list(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    categories = genre.categories.all()

    return render(request, 'notes/category_list.html', {'genre': genre, 'categories': categories})

# 本文一覧
def content_list(request, genre_name, category_name):
    genre = get_object_or_404(Genre, name=genre_name)
    category = get_object_or_404(Category, name=category_name)
    contents = category.contents.all()

    return render(request, 'notes/content_list.html', {'genre': genre, 'category': category, 'contents': contents})

# 本文詳細
def content_detail(request, genre_name, category_name, content_id):
    genre = get_object_or_404(Genre, name=genre_name)
    category = get_object_or_404(Category, name=category_name, genre=genre)
    content = get_object_or_404(Content, id=content_id, category=category)

    return render(request, 'notes/content_detail.html', {'genre': genre, 'category': category, 'content': content})