from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = ['About', 'Add article', 'Feedback', 'Login']


def index(request):  # http://127.0.0.1:8000/women/
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})


def about(request):  # http://127.0.0.1:8000/women/about/
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})


def categories(request, catid):  # http://127.0.0.1:8000/women/cats/
    if request.GET:
        print(request.GET)
    return HttpResponse(f"Content by categories {catid}")


def archive(request, year):  # http://127.0.0.1:8000/women/archive/9999/
    if int(year) >= 2023:
        return redirect('women_home_page', permanent=True)  # 301
    # return redirect('/women') 304
    # raise Http404()
    return HttpResponse(f"Content archived from {year}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Page not found.")