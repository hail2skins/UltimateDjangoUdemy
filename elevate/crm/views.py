from django.shortcuts import render
from django.http import HttpResponse # Add this import to allow for an HTTP response

# Create your views here.

def home(request):
    return render(request, 'crm/index.html') # Add this function to render the index.html template


def register(request):
    return render(request, 'crm/register.html') # Add this function to render the register.html template
