from django.db import models

# Create your models here.

class tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    tasks_desc = models.TextField()
    status = models.CharField(max_length=50, default="In Progress")
    user_id = models.IntegerField()

