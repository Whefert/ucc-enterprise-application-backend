from .models import Address
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def all_addresses(request):
    # query the database for all addresses
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)

# Get all students
@api_view(['GET'])
def all_students(request):
    # query the database for all students
    students = Student.objects.all()

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# Get all users
@api_view(['GET'])
def all_users(request):
    # query the database for all users
    users = User.objects.select_related('title', 'address', 'contact_details', 'next_of_kin1').all()
    serializer = UserSerializer(users, many=True, )
    return Response(serializer.data)

# Get a student
@api_view(['GET'])
def get_student(request, id):
    # query the database for a student
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

# Get student courses
@api_view(['GET'])
def student_courses(request, id):
    # query the databse for all course enrollments for a student
    courses = CourseEnrollment.objects.filter(student_id=id)
    serializer = CourseEnrollmentSerializer(courses, many=True)
    return Response(serializer.data)


# Get all courses
@api_view(['GET'])
def all_courses(request):
    # query the database for all courses
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# Get a course
@api_view(['GET'])
def get_course(request, id):
    # query the database for a course
    course = Course.objects.get(id=id)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)

# Get all faculty
@api_view(['GET'])
def all_faculty(request):
    # query the database for all staff that have a position of Lecturer
    faculty = Staff.objects.filter(position__name='Lecturer')
    
    serializer = StaffSerializer(faculty, many=True)
    return Response(serializer.data)

# Get a member of faculty
@api_view(['GET'])
def get_staff(request, id):
    # query the database for a staff member
    staff = Staff.objects.get(id=id)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)