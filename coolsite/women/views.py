from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):  # http://127.0.0.1:8000/women/
    return HttpResponse("Women's app page.")


def categories(request):  # http://127.0.0.1:8000/cats/
    return HttpResponse("Content by categories")
