from django.shortcuts import render_to_response,render
from django.http import HttpResponse

def index(request):
    # return render_to_response("home.html")
    # return HttpResponse("line")
    return render(request, "index.html")

def home(request):
    return render(request, 'home.html')

def list(request):
    return render(request, 'list.html')

# Create your views here.
