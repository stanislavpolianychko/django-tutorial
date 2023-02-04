from django.urls import path, re_path

from women.views import *

urlpatterns = [
    path('', index, name='women_home_page'),
    path('about/', about, name='about')
]
