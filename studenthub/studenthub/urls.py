from django.contrib import admin
from django.urls import path, include
from student_management_app import views
from django.conf.urls.static import static
from studenthub import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_home),
    path('home/',include('student_management_app.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


