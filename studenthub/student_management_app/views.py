import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt
import math
from .EmailBackEnd import EmailBackEnd
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
# Create your views here.


def login_home(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return render(request,'admin_home.html')
        elif request.user.user_type == '2':
            return redirect(reverse("staff_home"))
        else:
            return redirect(reverse("student_app:profile"))
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
                return redirect(reverse("student_app:profile"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")
    


def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")



# def profile(request):
#     user=Student.objects.get(email=request.user.email)
#     # user=CustomUser.objects.all().filter(email=request.user.email)
#     # student=get_object_or_404(CustomUser, id=user.student_id)
#     # student = get_object_or_404(Student, admin=request.user)
#     # username=student.email
#     # username=user.email
#     if request.user != None:
#         return render(request,'profile.html', {'email': user.email})

# def profile(request):
#     student = get_object_or_404(Student, admin=request.user)
#     name = student.first_name + ", " + student.last_name 
#     total_subject = Subject.objects.filter(course=student.course).count()
#     total_attendance = AttendanceReport.objects.filter(student=student).count()
#     total_present = AttendanceReport.objects.filter(student=student, status=True).count()

     
    
#     if total_attendance == 0:
#         subject_name = []
#         data_present = []
#         data_absent = []
#         subjects = Subject.objects.filter(course=student.course)
#     for subject in subjects:
#         attendance = Attendance.objects.filter(subject=subject)
#         present_count = AttendanceReport.objects.filter(
#             attendance__in=attendance, status=True, student=student).count()
#         absent_count = AttendanceReport.objects.filter(
#             attendance__in=attendance, status=False, student=student).count()
#         subject_name.append(subject.name)
#         data_present.append(present_count)
#         data_absent.append(absent_count)
       
#     context = {
#         'name': name,
#         'total_attendance': total_attendance,
#         'total_subject': total_subject,
#         'subjects': subjects,
#         'data_present': data_present,
#         'data_absent': data_absent,
#         'data_name': subject_name,
#         'page_title': 'Student Homepage'}

#     return render(request, 'profile.html', context) # Don't divide. DivisionByZero

def profile(request):
    user = CustomUser.objects.get(email=request.user.email)
    first_name = user.first_name
    last_name = user.last_name
    # semester = student.session
    g = ""
    gender = user.gender
    if gender == "M":
        g = "Male"
    else:
        g = "Female"  

    image = user.profile_pic  
    address = user.address
    email_id = user.email
    return render(request, "profile.html", {'first_name':first_name,'last_name':last_name,'gender':g,'image':image,'address':address,'email':email_id})
       
        
def gradePointCalc(grade):
	if(grade == "A"):
		gradePoint = 4
	elif ( grade == "A-"):
		gradePoint = 3.5