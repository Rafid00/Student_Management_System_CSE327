from django.urls import path, include

from . import adminviews
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from . import staffviews
app_name = 'student_app'
urlpatterns = [
    path('', views.login_home,  name='login_home'),
#     path('studentprofile/', views.student_profile, name='student_profile'),
#     path('facultyprofile/', views.faculty_profile, name='faculty_profile'),
    path('main/', views.login_home, name='main'),
    path('dologin/', views.doLogin, name='dologin'),
    path('adhome/', adminviews.admin_home, name='adminview'),
    path('addstd/', adminviews.add_student, name='add_student'),
    path('addfac/', adminviews.add_staff, name='add_faculty'),
    path('sendnotice/', adminviews.send_notice, name='send_notice'),
    path("view_attendance/", adminviews.admin_view_attendance, name="admin_view_attendance",),
    path("fetch_attendance/", adminviews.get_admin_attendance, name='get_admin_attendance'),
    path('Logout/', views.logout_user, name='logout_admin'),
    path('add_course/',adminviews.add_course,name='add_course'),
    path('add_student/', adminviews.add_student,name="add_student_save"),
    path('add_semester/',adminviews.add_semester,name='add_semester'),
    path('edit_student/<int:student_id>',adminviews.edit_student,name='edit_student'),
    path('manage_student/',adminviews.manage_student,name='manage_student'),
    path('manage_staff/',adminviews.manage_staff,name='manage_staff'),
    path('manage_course/',adminviews.manage_course,name='manage_course'),
    path('manage_semester/',adminviews.manage_semester,name='manage_semester'),
    path('edit_staff/<int:staff_id>',adminviews.edit_staff,name='edit_staff'),
    path('edit_semester/<int:session_id>',adminviews.edit_semester,name='edit_semester'),
    path('edit_course/<int:course_id>',adminviews.edit_course,name='edit_course'),
    path("send_student_notice/", adminviews.send_student_notification,
         name='send_student_notice'),
    path("send_staff_notice/", adminviews.send_staff_notification,
         name='send_staff_notice'),
    path('logout_user/', views.logout_user, name="logout_user"),
    path("check_email_availability",adminviews.check_email_availability,
         name="check_email_availability"),
    path('staff_home/', views.staff_profile, name='staff_home'),
    path('staff_take_attendance/',staffviews.staff_take_attendance,name="staff_take_attendance"),
    path('staff_update_attendance/',staffviews.staff_update_attendance,name="staff_update_attendance"),
    path('profile/', views.profile, name='profile'),
    path("staff_get_students/", staffviews.get_students, name='get_students'),
    path("staff_save_attendance/", staffviews.save_attendance, name='save_attendance'),
    path("get_attendance", views.get_attendance, name='get_attendance'),
    path("staff_attendance_update/",
         staffviews.update_attendance, name='update_attendance'),
    path('add_payment/',adminviews.payment_status,name='add_payment'),
    path('update_payment/<int:student_id>',adminviews.update_payment_status,name='update_payment'),
]
