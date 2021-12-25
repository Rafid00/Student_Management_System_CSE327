from django.contrib import admin
from student_management_app.models import Courses, CustomUser, SemesterModel, Students
from student_management_app.models import Attendance
from student_management_app.models import Staffs
from student_management_app.models import Subjects
from student_management_app.models import NotificationStudent
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(Attendance)
admin.site.register(Staffs)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(NotificationStudent)
admin.site.register(Courses)
admin.site.register(SemesterModel)