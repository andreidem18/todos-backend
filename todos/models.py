from django.db import models

from priorities.models import Priority

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField()
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    deadline = models.DateField(models.DateField(auto_now=True))

    def __str__(self):
        return self.title
