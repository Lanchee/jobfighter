from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    # return render_to_response("home.html")
    # return HttpResponse("line")
    return render(request, "index.html")


def home(request):
    return render(request, 'home.html')


def list(request, skill):
    return HttpResponse("the param is:" + skill)
    # return render(request, 'list.html')

def skill(request):
    skill = request.GET.get('skills')
    return HttpResponse("the param is:" + skill)

# Create your views here.
