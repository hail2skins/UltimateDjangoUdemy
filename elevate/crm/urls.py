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
    path('update-task/<str:pk>/', views.update_task, name="update-task"), # Add this line to map the task_update view to the task_update URL
    path('delete-task/<str:pk>/', views.delete_task, name="delete-task"), # Add this line to map the task_delete view to the task_delete URL
    path('show-task/<str:pk>/', views.show_task, name="show-task"), # Add this line to map the task_show view to the task_show URL
    path('login', views.login, name="login"), # Add this line to map the login view to the login URL
    path('dashboard', views.dashboard, name="dashboard"), # Add this line to map the dashboard view to the dashboard URL
    path('logout', views.logout, name="logout"), # Add this line to map the logout view to the logout URL
]