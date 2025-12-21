from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h1>Online Shope Home Page</h>")

def about(request):
    return HttpResponse("<h1>Online Shope About Page</h>")