from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import  User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="signin")
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
     
     if request.method == "POST":
          username = request.POST.get('username')
          email = request.POST.get('email')
          pswd = request.POST.get('pswd')

          myuser = User.objects.create_user(username,email,pswd)
          myuser.name = username
          myuser.save()
          messages.success(request,"Your account has been successfully created")
          return redirect("signin")
          
     return render(request,"authentication\signup.html")   

def signin(request):
     if request.method == "POST":
          username = request.POST.get("username")
          pswd = request.POST.get("pswd")
          print(username,pswd)
          
          user =  authenticate(request,username = username,password = pswd)

          if user is not None:
               login(request,user)
               return redirect("home")
          else:
               return HttpResponse("user name or password is incorrect")
     return render(request,"authentication/login.html")

def signout(request):
     logout(request)
     return redirect("signin")

