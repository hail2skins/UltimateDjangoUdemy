from django.shortcuts import render
from django.http import HttpResponse # Add this import to allow for an HTTP response

# Create your views here.

def home(request):
    return HttpResponse("This is the home page") # Add this function to return an HTTP response


def register(request):
    return HttpResponse("This is the registration page") # Add this function to return an HTTP response
