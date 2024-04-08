from django.shortcuts import render
from django.http import HttpResponse # Add this import to allow for an HTTP response
from .models import Task # import the Task model

# Create your views here.

def home(request):
    
    client_list = [
        {
            'id': 1,
            'name': 'John Doe',
            'occupation': 'Web Developer',
        },
        {
            'id': 2,
            'name': 'Kate Smith',
            'occupation': 'Attorney',
        },
    ]
    
    examList = [
        {
            'id': 1,
            'name': 'Science',
            'grade': '12',
        },
        {
            'id': 2,
            'name': 'Math',
            'grade': '10',
        },
    ]
    
    context = {
        'first_name': 'Art',
        'client_list': client_list,
        'examList': examList,
    }
    
    return render(request, 'crm/index.html', context) # Add this function to render the index.html template


def register(request):
    return render(request, 'crm/register.html') # Add this function to render the register.html template

def task(request):
    
    # Get a single task object from the database
    task = Task.objects.get(id=3)
    
    context = {
        'task': task,
    }
        

def getAllTasks(request):
    
    # Get all task objects from the database
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
    }
    
    return render(request, 'crm/tasks.html', context) # Add this function to render the tasks.html template