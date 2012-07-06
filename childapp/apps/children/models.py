from django.db import models
from django.contrib.auth.models import User

from childapp.apps.children.constants import GENDER_CHOICES

class Child(models.Model):
    parent = models.ForeignKey(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=200, choices = GENDER_CHOICES)
