# Here we must define paths to different web pages

from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name = "index"), # this code serves the http response from the views.py
    path("about", views.about, name = "about"),
]