from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    #this simple line grabs all objects from the database for Project model
    #that is defined in models.py of this app! it is that simple!!
    context = {'projects': projects}
    return render(request, "portfolio/home.html", context)
    