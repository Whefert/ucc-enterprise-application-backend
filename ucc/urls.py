"""
URL configuration for ucc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('address/', views.all_addresses),
    # Get all students
    path('student/', views.all_students),
    # Get student courses
    path('student/<int:id>/courses/', views.student_courses),

    # Get a student
    path('student/<int:id>/', views.get_student),
    path('user/', views.all_users),
    # Get al courses
    path('course/', views.all_courses),
    # Get a course
    path('course/<int:id>/', views.get_course),
    # Get faculty
    path('faculty/', views.all_faculty),
    # Get a member of faculty
    path('staff/<int:id>/', views.get_staff),



]

