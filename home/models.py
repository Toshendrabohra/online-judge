from cgi import test
from operator import truediv
from django.db import models 
from django.db.models.fields import CharField, NullBooleanField,TextField
from django.utils import timezone 
from django.contrib.auth.models import User 
# Create your models here.

class Problemset(models.Model):
        problem_id=models.BigAutoField(primary_key=True)
        problem_name=models.CharField(max_length=100)
        difficulty=models.CharField(max_length=100)
        statement=models.TextField()

        def __int__(self):
                return self.problem_id
        

class Submission(models.Model):
        submission_id=models.BigAutoField(primary_key=True)
        user_id=models.ForeignKey(User,on_delete=models.CASCADE)
        problem_id=models.ForeignKey(Problemset, on_delete=models.CASCADE)
        verdict=models.CharField(max_length=100)
        submission_time=models.DateTimeField(default=timezone.now)
        user_submission=models.TextField()
        problem_name=models.CharField(max_length=100)

        def __int__(self):
                return self.submission_id
        class meta:
                ordering = ('submission_time',)


class Testcase(models.Model):
        testcase_id=models.BigAutoField(primary_key=True)
        problem_id=models.ForeignKey(Problemset, on_delete=models.CASCADE)
        input=models.TextField()
        output=models.TextField()

        def __int__(self):
                return self.testcase_id



