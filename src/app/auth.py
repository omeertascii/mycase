from django.contrib.auth.models import User
from django.db import models

class WorkGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='workgroups')