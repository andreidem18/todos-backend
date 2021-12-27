from django.db import models

class Priority(models.Model):
    priority = models.CharField(max_length=100)

    def __str__(self):
        return self.priority
