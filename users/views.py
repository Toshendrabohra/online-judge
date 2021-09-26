from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http.request import HttpRequest
from django.http import HttpResponse
from django .contrib import messages
from .forms import UserRegisterForm
def register(request):
    if request.method =='POST':
         form =UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request,f'Account has been Created for {username} .')
             return redirect('login')
    else:
         form =UserRegisterForm()
    return render(request,'users/register.html',{'form':form})