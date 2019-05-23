from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info/index.html', {'nbar': 'home'})
    # return HttpResponse("Hello, world! You're in the info index.")

def about(request):
    return render(request, 'info/about.html', {'nbar': 'about'})

def projects(request):
    return render(request, 'info/projects.html', {'nbar': 'projects'})

def contact(request):
    return render(request, 'info/contact.html', {'nbar': 'contact'})
