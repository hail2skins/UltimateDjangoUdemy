# Will hold all model forms
# Imports
from django.forms import ModelForm # Allos access to the ModelForm class. Magic stuff here
from .models import Task # import the Task model

# for user registration
from django.contrib.auth.forms import UserCreationForm # Allows access to the UserCreationForm class
from django.contrib.auth.models import User # Allows access to the User model, the django built-in user model

# for user login
from django.contrib.auth.forms import AuthenticationForm # Allows access to the AuthenticationForm class
from django import forms # Allows access to the forms module
from django.forms.widgets import PasswordInput # Allows access to the PasswordInput widget
from django.forms.widgets import TextInput # Allows access to the Text widget

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

# Create a login form from AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})) # Set the username field to a CharField with TextInput widget
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) # Set the password field to a CharField with PasswordInput widget