from . import views

from django.urls import path, include

app_name = 'zillion'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('articles', views.articles, name = 'articles'),
    path('news', views.news, name = 'news'),
    path('books', views.books, name = 'books'),
]
