from django.shortcuts import render

# Create your views here.

# stores different views for the application HTTP requests

def index(request):
    return render(request, "main/home.html", {})
