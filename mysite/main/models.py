from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
