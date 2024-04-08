from django.shortcuts import render, redirect # Add this import to allow for rendering and redirection
from django.http import HttpResponse # Add this import to allow for an HTTP response
from .models import Task # import the Task model
from .forms import TaskForm # import the TaskForm model

# Create your views here.

# Homepage view
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

# CRUD operations - Create a task
def create_task(request):
    form = TaskForm() # Create a new instance of the TaskForm model
    
    # Check if the form has been submitted using if statement
    if request.method == 'POST':
        form = TaskForm(request.POST) # Create a new instance of the TaskForm model with the POST data
        
        # Check if the form is valid using if statement
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('view-tasks') # Redirect to the task view            
    
    context = {
        'form': form,
    }
    return render(request, 'crm/create-task.html', context) # Add this function to render the task_form.html template

#CRUD operations - View all tasks
def tasks(request):
    
    # Get all tasks from the database
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
    }
    
    return render(request, 'crm/view-tasks.html', context) # Add this function to render the task.html template
        

# Register view
def register(request):
    return render(request, 'crm/register.html') # Add this function to render the register.html template