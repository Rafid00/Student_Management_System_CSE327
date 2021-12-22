from django.urls import path, include
from . import views
app_name = 'student_app'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_home, name='login_home'),
    path('main/', views.home, name='main'),
    path('dologin/', views.doLogin, name='dologin'),
    path('adhome/', views.adminview, name='adminview'),
    path('managestd/', views.manage_student, name='manage_student'),
    path('managefac/', views.manage_facutly, name='manage_faculty'),
    path('advising/', views.advising, name='advising'),
    path('sendnotice/', views.send_notice, name='sendnotice'),
    path('Logout/', views.logout_admin, name='logout_admin'),
]