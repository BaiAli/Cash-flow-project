from django.db import models
class TodoListItem(models.Model):
    content = models.TextField() 

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
