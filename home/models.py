from cgi import test
from operator import truediv
from django.db import models 
from django.db.models.fields import CharField, NullBooleanField,TextField
from django.utils import timezone 
from django.contrib.auth.models import User 
import uuid
# Create your models here.

class Problemset(models.Model):
        problem_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        problem_name=models.CharField(max_length=100)
        difficulty=models.CharField(max_length=100)
        statement=models.TextField()
        input_format=models.TextField()
        output_format=models.TextField()

        def __str__(self):
                return self.problem_name
        


class Submission(models.Model):
        submission_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user_id=models.ForeignKey(User,on_delete=models.CASCADE)
        problem_id=models.ForeignKey(Problemset, on_delete=models.CASCADE)
        verdict=models.CharField(max_length=100)
        submission_time=models.DateTimeField(default=timezone.now)
        user_submission=models.TextField()
        problem_name=models.CharField(max_length=100)

        languages = [
                ("cpp", "C++"),
                ("java", "Java"),
                ("py", "Python"),
        ]
        language=models.CharField(max_length=5,choices=languages, default = "C++")

        def __str__(self):
                return self.user_id + "-" + self.problem_name + "-" + self.verdict
        class meta:
                ordering = ('submission_time',)


class Testcase(models.Model):
        testcase_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        problem_id=models.ForeignKey(Problemset, on_delete=models.CASCADE)
        input=models.TextField()
        output=models.TextField()
        sample=models.BooleanField(default=False)

        def __uuid__(self):
                return self.testcase_id



