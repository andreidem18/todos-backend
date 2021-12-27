from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField(models.DateField(auto_now=True))

    def __str__(self):
        return self.title