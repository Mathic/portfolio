from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'info/index.html')
    # return HttpResponse("Hello, world! You're in the info index.")

def about(request):
    return render(request, 'info/about.html')

def projects(request):
    return render(request, 'info/projects.html')

def contact(request):
    return render(request, 'info/contact.html')
