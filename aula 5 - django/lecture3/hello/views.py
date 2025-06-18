from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def luiz(request):
    return HttpResponse("Hello, Luiz!")

def perla(request):
    return HttpResponse("Hello, Perla!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })