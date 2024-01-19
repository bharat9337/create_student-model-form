from django.db import models

# Create your models here.
from app.models import *

from django.core import validators




class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


    def __str__(self):
        return self.Sname