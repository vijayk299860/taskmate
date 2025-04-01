from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['id', ]