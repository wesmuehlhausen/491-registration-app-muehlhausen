from django.db import models
from django.core import validators
from django.core.validators import MinimumLengthValidator, MaximumLengthValidator

class Student(models.Model):
    studentid = models.PositiveIntegerField(blank=True)
    firstname = models.CharField(max_length=50)
    


# Create your models here.
