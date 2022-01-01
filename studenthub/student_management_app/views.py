import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from .EmailBackEnd import EmailBackEnd
from .models import *

# Create your views here.


def login_home(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return render(request,'admin_home.html')
        elif request.user.user_type == '2':
            return redirect(reverse("staff_home"))
        else:
            return redirect(reverse("student_home"))
    return render(request, 'login.html')


def doLogin(request, **kwargs):
    if request.method != 'POST':
        return HttpResponse("<h4>Denied</h4>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)

            file1 = open("student_management_app\\tempdata.txt","w") #write mode
            file1.write(request.POST.get('email'))
            file1.close()
            
            if user.user_type == '1':
                return render(request,'admin_home.html')
            elif user.user_type == '2':
                return redirect(reverse("staff_home"))
            else:
                return redirect(reverse("student_home"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")
    


def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")


def profile(request):
    user=CustomUser.objects.get(email=request.user.email)
    # user=CustomUser.objects.all().filter(email=request.user.email)
    # student=get_object_or_404(CustomUser, id=user.student_id)
    # student = get_object_or_404(Student, admin=request.user)
    # username=student.email
    # username=user.email
    if request.user != None:
        return render(request,'profile.html', {'email': user.email})

