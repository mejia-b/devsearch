from django.shortcuts import render
from django.http import HttpResponse

# Functions get called depending on the url name

def projects(request):
    return render(request,'projects/projects.html')

def project(request,pk):
    return render(request,'projects/single-project.html')