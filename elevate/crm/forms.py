# Will hold all model forms
# Imports
from django.forms import ModelForm # Allos access to the ModelForm class. Magic stuff here
from .models import Task # import the Task model

from django.contrib.auth.forms import UserCreationForm # Allows access to the UserCreationForm class
from django.contrib.auth.models import User # Allows access to the User model, the django built-in user model

# Create a class that inherits from ModelForm
class TaskForm(ModelForm):
    class Meta:
        model = Task # Set the model to Task
        fields = '__all__' # Set the fields to '__all__' which means all available fields in the model, but not ID or CreatedAt stuff like that
        
# Create a class that inherits from UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User # Set the model to User
        fields = ['username', 'email', 'password1', 'password2'] # Set the fields to ['username', 'email', 'password1', 'password2'] which are the fields in the User model
