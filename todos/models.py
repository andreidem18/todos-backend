from django.db import models

from priorities.models import Priority

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_complete = models.BooleanField()

    def __str__(self):
        return self.title
