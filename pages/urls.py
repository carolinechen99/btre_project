from django.urls import path

# Have an url that is attached to a method in views.py
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),# path(''(root path/home page), method called from views.py, name of the url)
    path('about', views.about, name = 'about')
]
