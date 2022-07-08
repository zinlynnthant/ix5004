from django import http
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def articles(request):
    return render(request, 'articles.html')

def books(request):
    return render(request, 'books.html')

def news(request):
    return render(request, 'news.html')

def handler(request, exception):
    return http.HttpResponse("{% url 'error.html' %}")