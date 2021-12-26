from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
import os

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_management_app.EmailBackEnd import EmailBackEnd
from student_management_app.models import CustomUser, Courses, SemesterModel
from studenthub import settings

# Create your views here.

def login_home(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
    if user!=None:
            login(request,user)
            if user.user_type=="1":
                return render(request, 'home.html')
            elif user.user_type=="2":
               return render(request, 'login.html')
            else:
                return render(request, 'login.html')
    else:
        messages.error(request,"Invalid Login Details")
        return render(request, 'login.html') 
            



def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return render(request,'login.html')

def signup_admin(request):
    return render(request,"signup_admin_page.html")

def signup_student(request):
    courses=Courses.objects.all()
    session_years=SemesterModel.object.all()
    return render(request,"signup_student_page.html",{"courses":courses,"session_years":session_years})

def signup_staff(request):
    return render(request,"signup_staff_page.html")

def adminview(request):
    return render(request,'admin_view.html')

def manage_student(request):
    return render(request,'manage_student.html')

def manage_facutly(request):
     return render(request,'manage_faculty.html')

def advising(request):
     return render(request,'advising.html')

def logout_admin(request):
    return render(request, 'login.html')

def send_notice(request):
    return render(request,'sendnotice.html')


