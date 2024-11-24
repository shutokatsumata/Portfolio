from django.urls import path
from . import views

urlpatterns = [
    # ジャンル一覧
    path('', views.genre_list, name='genre_list'),
    # カテゴリ一覧
    path('<str:genre_name>/', views.category_list, name='category_list'),
    # 本文一覧
    path('<str:genre_name>/<str:category_name>/', views.content_list, name='content_list'),
    # 本文詳細
    path('<str:genre_name>/<str:category_name>/<int:content_id>/', views.content_detail, name='content_detail'),
]