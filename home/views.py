from asyncio.subprocess import PIPE
from cgi import test
from operator import is_
from re import sub
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
@login_required
def index(request):
    context = {
        'problems' : Problemset.objects.all()
    }
    return render(request,'home/index.html',context)

def leaderboard(request):
     latest =Submission.objects.all()
     context = {
        "submissions": latest
     }
     return render(request,'home/leaderboard.html',context)

def problem_page(request,pid):
    context ={
        'prblm' :Problemset.objects.get(problem_id=pid)
    }
    return render(request,'home/problem_page.html',context)


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
    # print(os.getcwd()) #prints cur directory
    os.chdir('newcpp')
    file = open('code.cpp', 'w')
    file.write(code)
    file.close()
    subprocess.run(['docker', 'stop', 'compiler'])
    run_container = subprocess.run(['docker', 'run', '-d', '-t', '--rm', '--name', 'compiler', 'saitama26/oj_sandbox'])
    copy_code = subprocess.run(['docker', 'cp', 'code.cpp', 'compiler:/in_container'])
    executable = subprocess.run(['docker', 'exec', 'compiler','g++', '-o', 'executable_file' ,'code.cpp'], capture_output=True, text=True,shell=True)
    if run_container.returncode == 1 or copy_code.returncode == 1:
        return " ServerError "
    testcases = Testcase.objects.filter(problem_id = problem)
    is_correct = True   
    is_compile_error = False
    if executable.returncode == 1:
        is_correct = False
        is_compile_error = True
        err_msg = executable.stderr
    if not is_compile_error :        
        for testcase in testcases:
            stdout = run_tests(testcase)
            if not stdout[0]:
                is_correct = stdout[0]
                err_msg = stdout[1]
                break
    if not is_correct:
        if not is_compile_error:
            verdict = "wrong answer :( \n your output {}".format(err_msg)
        else:
            verdict = "Compile error :( " + err_msg
    else:
        verdict = "Accepted"
    subprocess.run(['docker', 'stop', 'compiler'])
    os.chdir('..')
    return verdict
    

def run_tests(testcase):
    file_input = open('input.txt', 'w')
    file_input.write(testcase.input)
    file_input.close()
    file_output = open('std_output.txt', 'w')
    file_output.write(testcase.output)
    file_output.close()

    #copy input.txt
    subprocess.run(['docker', 'cp', 'input.txt', 'compiler:/in_container']) 
    #to create output.txt inside container
    subprocess.run(['docker', 'cp', 'output.txt', 'compiler:/in_container'])

    output_generation = subprocess.run(f'docker exec compiler sh -c "./executable_file <input.txt> output.txt"',shell=True)
    if output_generation.returncode == 1:
        return False

    #to copy generated ouput    
    subprocess.run(['docker', 'cp', 'compiler:/in_container/output.txt', 'output.txt'])
    diff = subprocess.run("FC /W std_output.txt output.txt", shell=True, capture_output=True)    
    text_file = open("output.txt", "r")
    data = text_file.read()
    text_file.close()
    return [diff.returncode == 0, data]
    
   
   
    