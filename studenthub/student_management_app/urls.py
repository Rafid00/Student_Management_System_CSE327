from django.urls import path, include
from . import views
app_name = 'student_app'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_home, name='login_home'),
    path('main/', views.home, name='home'),
]