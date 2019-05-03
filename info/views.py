from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'info/index.html')
    # return HttpResponse("Hello, world! You're in the info index.")
