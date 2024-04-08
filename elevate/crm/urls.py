# App urls.py file
# Path: elevate/crm/urls.py
# Imports
from django.urls import path # Add this import to allow for path routing

from . import views # Import the views from the current directory


# URL patterns
urlpatterns = [
    path('', views.home, name=""), # Add this line to map the root URL to the index view
    
    path('register/', views.register, name="register"), # Add this line to map the register view to the register URL
    path('view-tasks', views.tasks, name="view-tasks"), # Add this line to map the task view to the task URL
    path('create-task', views.create_task, name="create-task"), # Add this line to map the task_form view to the task_form URL
]