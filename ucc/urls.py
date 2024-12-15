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
    # Login
    path('login/', views.login),

    # Get a student
    path('student/<int:id>/', views.get_student),
    path('user/', views.all_users),
    # Get all courses
    path('course/', views.all_courses),
    # Get a course
    path('course/<int:id>/', views.get_course),
    # Get all course enrollments
    path('course_enrollment/', views.all_course_enrollments),
    # Get a course enrollment
    path('course_enrollment/<int:id>/', views.course_enrollment),
    # Get faculty
    path('faculty/', views.all_faculty),
    # Get a member of faculty
    path('staff/<int:id>/', views.get_staff),
    # Get enrollment status
    path('enrollment_status/', views.all_enrollment_status),
    # Get all programs of study
    path('program_of_study/', views.all_program_of_study),
    # Get all departments
    path('department/', views.all_departments),
    # Get all positions
    path('position/', views.all_positions),
    # Get all course schedule lecturers
    path('course_schedule_lecturer/', views.all_course_schedule_lecturer),
    # Get all course schedules taught by a lecturer
    path('course_schedule_lecturer/<int:id>/', views.course_schedule_lecturer),
    # Get course prerequisites
    path('course/<int:id>/prerequisites/', views.course_prerequisites),

]

