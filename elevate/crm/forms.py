# Will hold all model forms
# Imports
from django.forms import ModelForm # Allos access to the ModelForm class. Magic stuff here
from .models import Task # import the Task model

# Create a class that inherits from ModelForm
class TaskForm(ModelForm):
    class Meta:
        model = Task # Set the model to Task
        fields = '__all__' # Set the fields to '__all__' which means all available fields in the model, but not ID or CreatedAt stuff like that
        
    
