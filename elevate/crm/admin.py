from django.contrib import admin
from . models import Task # import the Task model
from . models import Review # import the Review model

# Register your models here.
admin.site.register(Task) # register the Task model
admin.site.register(Review) # register the Review model