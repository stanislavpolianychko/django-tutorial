import django.shortcuts
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):  # http://127.0.0.1:8000/women/
    return HttpResponse("Women's app page.")


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