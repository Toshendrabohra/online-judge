from django.db import models
from django.db.models.fields import CharField, NullBooleanField,TextField
from django.utils import timezone 
from django.contrib.auth.models import User 
# Create your models here.
class problemset(models.Model):
        problemid=models.IntegerField()
        problemName=models.CharField(max_length=100)
        difficulty=models.CharField(max_length=100)
        statement=models.TextField()

        def __int__(self):
            return self.problemid

class solutions(models.Model):
        problemid=models.CharField(max_length=100)
        userid=models.CharField(max_length=100)
        verdict=models.CharField(max_length=100)
        submitTime=models.DateTimeField(default=timezone.now)
        usersolution=models.TextField()
        problemname=models.CharField(max_length=100)

class testcase(models.Model):
        problemid=models.CharField(max_length=100)
        input=models.TextField()
        output=models.TextField()





