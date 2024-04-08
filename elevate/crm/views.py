from django.shortcuts import render, redirect # Add this import to allow for rendering and redirection
from django.http import HttpResponse # Add this import to allow for an HTTP response
from .models import Task # import the Task model
from .forms import TaskForm # import the TaskForm model

# for user registration
from .forms import CreateUserForm # import the CreateUserForm model
from .forms import LoginForm # import the LoginForm model

# for user login
from django.contrib.auth.models import auth # import the auth model
from django.contrib.auth import authenticate, login, logout # import the authenticate and login functions

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
   
#CRUD operations - Update a task
def update_task(request, pk):
    
    # Get the task with the primary key (pk) from the database
    task = Task.objects.get(id=pk)
    
    # Create a new instance of the TaskForm model with the task data
    form = TaskForm(instance=task)
    
    # Check if the form has been submitted using if statement
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # Create a new instance of the TaskForm model with the POST data and task data
        
        # Check if the form is valid using if statement
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('view-tasks') # Redirect to the task view
    
    context = {
        'form': form,
    }
    
    return render(request, 'crm/update-task.html', context) # Add this function to render the task_form.html template

# CRUD operations - Delete a task
def delete_task(request, pk):
    
    # Get the task with the primary key (pk) from the database
    task = Task.objects.get(id=pk)
    
    # Check if the request method is POST using if statement
    if request.method == 'POST':
        task.delete() # Delete the task from the database
        return redirect('view-tasks') # Redirect to the task view
    
    context = {
        'task': task,
    }
    
    return render(request, 'crm/delete-task.html', context) # Add this function to render the delete_task.html template

# Show a single task
def show_task(request, pk):
    
    # Get the task with the primary key (pk) from the database
    task = Task.objects.get(id=pk)
    
    context = {
        'task': task,
    }
    
    return render(request, 'crm/show-task.html', context) # Add this function to render the show_task.html template

# Register view
def register(request):
    
    # Create a new instance of the CreateUserForm model
    form = CreateUserForm()
    
    # Check if the form has been submitted using if statement
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') #temporary until login page ready
    context = {
        'form': form,
    }
    
    return render(request, 'crm/register.html', context) # Add this function to render the register.html template

# Login view
def login(request):
    # Create a new instance of the LoginForm model
    form = LoginForm()
    
    # Check if the form has been submitted using if statement
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            # Check if user exists
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard') # Redirect to the dashboard view
    
    context = {
        'form': form,
    }
    
    
    return render(request, 'crm/login.html', context) # Add this function to render the login.html template

# Dashboard view
def dashboard(request):
    return render(request, 'crm/dashboard.html') # Add this function to render the dashboard.html template