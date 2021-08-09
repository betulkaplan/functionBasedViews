from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to FBV API</h1><center>')


# Create your views here.
