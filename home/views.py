from django.contrib.auth.signals import user_logged_in
from django.http.request import HttpRequest 
from django.http import Http404
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Problemset,Submission,Testcase,User
from django.contrib.auth.decorators import login_required
from .forms import UserSolution
import os
import subprocess

# Create your views here.

def index(request):
    context = {
        'problems' : Problemset.objects.all()
    }
    return render(request,'home/index.html',context)

def leaderboard(request):
     last =Submission.objects.all()
     latest = []
     for i in reversed(last):
        latest.append(i)
        if(len(latest) == 15):
            break
     context = {
        "submissions": latest
     }
     return render(request,'home/leaderboard.html',context)

def problem_page(request,pid):
    context ={
        'prblm' :Problemset.objects.get(problem_id=pid)
    }
    return render(request,'home/problem_page.html',context)

@login_required
def submit(request,pid):
    if request.method == 'POST':
         problem=Problemset.objects.get(problem_id=pid)
         code = request.POST.get('user_submission')
         current_user = User.objects.get(id=request.user.id)
         verdict_="wa"
         #checker(pid,code,current_user,problem.problem_id,code,Testcase.objects.get(problemid=problem.problemid).input, Testcase.objects.get(problemid=problem.problemid).output)
         submission=Submission(problem_id=problem, user_id=current_user, verdict=verdict_, user_submission=code, problem_name=problem.problem_name)
         submission.save()
    return redirect('leaderboard')
       
def checker(pid,code,current_user):
    
    os.chdir('newcpp')
    file=open('code.cpp','w')
    file.write(code)
    file.close()

    file_input = open('input.txt', 'w')
    file_input.write(input)
    file_input.close()
    file_output = open('output1.txt', 'w')
    file_output.write(output)
    file_output.close()
    #container_name=
  
    # write to STDIN as a byte object(convert string
    # to bytes with encoding utf8)
    os.write(temp, bytes(input, "utf-8"))
    os.close(temp)
  
    # store output of the program as a byte string in s
    s = subprocess.check_output("g++ -o out2 maintry.cpp  ; ./out2", stdin = data, shell = True)
   # os.system("docker cp my-running-app:/usr/src/compiler/output.txt output.txt")
   # os.system("docker stop my-running-app")
   
    flg = os.system("FC /W s.decode('utf-8') output1.txt")
    if flg == 1:
        verdict = "wrong answer"
    else:
        verdict = "accepted"
    os.chdir('..')
    return verdict