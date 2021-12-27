from django.db import models
from priorities.models import Priority
from todos.models import Todo

class Item(models.Model):
    item = models.CharField(max_length=100)
    todo = models.ForeignKey(Todo, on_delete=models.SET_NULL, null=True, related_name='items')
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    done = models.BooleanField()

    def __str__(self):
        return self.item
