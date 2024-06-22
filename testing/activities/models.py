from django.db import models

# Create your models here.
class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    description = models.TextField()