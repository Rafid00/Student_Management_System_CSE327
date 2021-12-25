from django.urls import path, include

from . import adminviews
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

app_name = 'student_app'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_home, name='login_home'),
    path('main/', views.home, name='main'),
    path('dologin/', views.doLogin, name='dologin'),
    path('adhome/', views.adminview, name='adminview'),
    path('addstd/', adminviews.add_student, name='add_student'),
    path('addfac/', adminviews.add_staff, name='add_faculty'),
    path('sendnotice/', views.send_notice, name='sendnotice'),
    path('Logout/', views.logout_admin, name='logout_admin'),
    path('add_course/',adminviews.add_course,name='add_course'),
    path('add_course_save/', adminviews.add_course_save,name="add_course_save"),
    path('add_student_save/', adminviews.add_student_save,name="add_student_save"),
    path('add_semester/',adminviews.add_semester,name='add_semester'),
     path('add_semester_save/',adminviews.add_semester_save,name="add_semester_save"),
    path('send_student_notice/',adminviews.send_student_notice,name='send_student_notice'),
    path('send_staff_notice/',adminviews.send_staff_notice,name='send_staff_notice'),
    path("check_email_exist/", adminviews.check_email_exist,
         name="check_email_exist"),
    path("check_username_exist/", adminviews.check_username_exist,
         name="check_username_exist"),
]