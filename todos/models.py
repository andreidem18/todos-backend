from django.db import models
from softdelete.models import SoftDeleteObject

class Todo(SoftDeleteObject, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isCompleted = models.BooleanField()
    created_by = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
