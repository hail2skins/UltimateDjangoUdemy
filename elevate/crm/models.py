from django.db import models

# Create your models here.
# Task model
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # string representation of the model in the admin panel
    def __str__(self):
        return self.title
    

# Review model
class Review(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE) # foreign key to Task model
    reviewer_name = models.CharField(max_length=200)
    review_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
        