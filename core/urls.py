from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    # トップページ
    path('', views.IndexView.as_view(), name='index'),
]