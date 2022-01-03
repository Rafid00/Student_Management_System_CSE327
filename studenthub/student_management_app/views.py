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
            return redirect(reverse("student_app:staff_home"))
        else:
            return redirect(reverse("student_app:student_home"))
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
                return redirect(reverse("student_app:staff_home"))
            else:
                return redirect(reverse("student_app:student_home"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")
    


def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")

@csrf_exempt
def get_attendance(request):
    subject_id = request.POST.get('subject')
    session_id = request.POST.get('session')
    try:
        subject = get_object_or_404(Subject, id=subject_id)
        session = get_object_or_404(Semester, id=session_id)
        attendance = Attendance.objects.filter(subject=subject, session=session)
        attendance_list = []
        for attd in attendance:
            data = {
                    "id": attd.id,
                    "attendance_date": str(attd.date),
                    "session": attd.session.id
                    }
            attendance_list.append(data)
        return JsonResponse(json.dumps(attendance_list), safe=False)
    except Exception as e:
        return None



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

def staff_profile(request):
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
    return render(request, "staff_home.html", {'first_name':first_name,'last_name':last_name,'gender':g,'image':image,'address':address,'email':email_id})


       
        
def gradePointCalc(grade):
    gradePoint = 1.234
    if grade == "A":
        gradePoint = 4.00
    elif grade == "A-":
        gradePoint = 3.50
    elif grade == "B+":
        gradePoint = 3.3
    elif grade == "B":
        gradePoint = 3.00
    elif grade == "B-":
        gradePoint = 2.70
    elif grade == "C+":
        gradePoint = 2.3
    elif grade == "C":
        gradePoint = 2
    elif grade == "C-":
        gradePoint = 1.7
    elif grade == "D":
        gradePoint = 1
    else:
        gradePoint = 0
    return gradePoint



# Create your views here.

# def Calculator_home(request):
#     if request.method == "POST":
#         cg_data = request.POST

#         if request.POST.get("passed_credits") != "":
#             credit_passed = int(request.POST.get("passed_credits"))

#             else:
#             credit_passed = 0
#         if request.POST.get("prev_cgpa") != "":
#             prev_cgpa = request.POST.get("prev_cgpa")
#             prev_cgpa = float(prev_cgpa.replace(' ', ''))
#         else:
#             prev_cgpa = 0

#         credits = []
#         for i in range(1, 6):
#             if request.POST.get(("credits" + str(i))) != "":
#                 credits.append(int(request.POST.get(("credits" + str(i)))))

#         grades = []
#         for i in range(1, 6):
#             if request.POST.get(("grade" + str(i))) != "":
#                 grades.append(gradePointCalc(request.POST.get(("grade" + str(i)))))

#         print("credits", credits)
#         print("grades", grades)

#         cg_credit_sum = 0

#         for i in range(len(credits)):
#             temp = grades[i] * credits[i]
#             cg_credit_sum += temp
#         new_cg = (float(prev_cgpa) * int(credit_passed) + float(cg_credit_sum)) / (int(credit_passed) + sum(credits))
#         context = {"cg_data": cg_data, "new_cg": new_cg}
#         return render(request, "cg_calculator/cg_calculator.html", context)
#     context = {}
#     return render(request, "cg_calculator/cg_calculator.html", context)
@csrf_exempt
def get_attendance(request):
    subject_id = request.POST.get('subject')
    session_id = request.POST.get('session')
    try:
        subject = get_object_or_404(Subject, id=subject_id)
        session = get_object_or_404(Semester, id=session_id)
        attendance = Attendance.objects.filter(subject=subject, session=session)
        attendance_list = []
        for attd in attendance:
            data = {
                    "id": attd.id,
                    "attendance_date": str(attd.date),
                    "session": attd.session.id
                    }
            attendance_list.append(data)
        return JsonResponse(json.dumps(attendance_list), safe=False)
    except Exception as e:
        return None


def cgpa_calculator(request):
    if request.method == "POST":
        cg_data = request.POST

        if request.POST.get("passed_credits") != "":
            credit_passed = int(request.POST.get("passed_credits"))
        else:
            credit_passed = 0
        if request.POST.get("prev_cgpa") != "":
            prev_cgpa = request.POST.get("prev_cgpa")
            prev_cgpa = float(prev_cgpa.replace(' ', ''))
        else:
            prev_cgpa = 0

        credits = []
        for i in range(1, 6):
            if request.POST.get(("credits" + str(i))) != "":
                credits.append(int(request.POST.get(("credits" + str(i)))))

        grades = []
        for i in range(1, 6):
            if request.POST.get(("grade" + str(i))) != "":
                grades.append(gradePointCalc(request.POST.get(("grade" + str(i)))))
 

        print("credits", credits)
        print("grades", grades)

        cg_credit_sum = 0

        for i in range(len(credits)):
            temp = grades[i] * credits[i]
            cg_credit_sum += temp
        new_cg = (float(prev_cgpa) * int(credit_passed) + float(cg_credit_sum)) / (int(credit_passed) + sum(credits))
        context = {"cg_data": cg_data, "new_cg": new_cg}
        return render(request, "cgpa_calculator.html", context)
    context = {}
    return render(request, "cgpa_calculator.html", context)

def student_home(request):
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
    email_id = user.email
    
    notice = Notice.objects.all()
    context = {
                'email': email_id,
                'notices':notice,
                'page_title':'Notice Overview'
                }
    return render(request, "student_home.html", context)

def notice_view(request):
    notices = Notice.objects.all()
    context = {'notices':notices,
                'page_title':'Notice Overview'
                }
    return render(request, "notice_overview.html", context)

def grade_overview(request):
    return render(request,"grade_overview.html")

def major_overview (request):
    context={'courses':[]}
    return render(request,"major_overview.html",context)

