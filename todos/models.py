from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isCompleted = models.BooleanField()
    created_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title
