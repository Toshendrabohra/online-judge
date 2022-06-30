from cgi import test
from operator import is_
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
         problem = Problemset.objects.get(problem_id = pid)
         code = request.POST.get('user_submission')
         current_user = User.objects.get(id = request.user.id)
         verdict_ = "wa"
         verdict_ = checker(problem, code)
         submission = Submission(problem_id = problem, user_id = current_user, verdict = verdict_, user_submission = code, problem_name = problem.problem_name)
         submission.save()
    return redirect('leaderboard')
       
def checker(problem, code):
    os.chdir('newcpp')
    file = open('code.cpp', 'w')
    file.write(code)
    file.close()
    subprocess.Popen(['g++', 'code.cpp'], shell=True)
    testcases = Testcase.objects.filter(problem_id = problem)
    is_correct = True
    is_compile_error = False
    compiler_err_msg = None
    for testcase in testcases:
        stdout = run_tests(testcase)
        if not stdout[0]:
            is_correct = stdout[0]
            is_compile_error = stdout[2]
            compiler_err_msg = stdout[1]
            break

    if not is_correct:
        if not is_compile_error:
            verdict = "wrong answer :("
        else:
            compiler_err_msg += "Compile error :("
            verdict = compiler_err_msg
    else:
        verdict = "Accepted"

    os.chdir('..')
    return verdict
    



def run_tests(testcase):
    file_input = open('input.txt', 'w')
    file_input.write(testcase.input)
    file_input.close()
    file_output = open('output.txt', 'w')
    file_output.write(testcase.output)
    file_output.close()
    pipedoutput = subprocess.run('a.exe',input=testcase.input, shell=True, capture_output=True, text=True)
    print('error', pipedoutput.stdout)
    return [pipedoutput.stdout.splitlines() == testcase.output.splitlines(), pipedoutput.stdout, pipedoutput.returncode != 0]
    # s = subprocess.check_output("g++ -o out2 maintry.cpp  ; ./out2", stdin = data, shell = True)
    # os.system("docker cp my-running-app:/usr/src/compiler/output.txt output.txt")
    # os.system("docker stop my-running-app")
   
    