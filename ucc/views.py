from .models import Address
from django.db.models import Q
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
    # query the database for enrolled student courses
    student_courses = CourseEnrollment.objects.filter(student_id=id)
    course_serializer = CourseEnrollmentSerializer(student_courses, many=True)

    # query the database for a student
    student = Student.objects.get(id=id)
    student_serializer = StudentSerializer(student, many=False)

    return Response({'student': student_serializer.data, 'courses': course_serializer.data})


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
    # query the database for all members of faculty. Check that the position is not staff (basic)
    faculty = Staff.objects.filter(~Q(position__name ='Staff'))
    
    serializer = StaffSerializer(faculty, many=True)
    return Response(serializer.data)

# Get a member of faculty
@api_view(['GET'])
def get_staff(request, id):
    # query the database for a staff member
    staff = Staff.objects.get(id=id)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)

# Get all enrollment status
@api_view(['GET'])
def all_enrollment_status(request):
    # query the database for all enrollment statuses
    statuses = EnrollmentStatus.objects.all()
    serializer = EnrollmentStatusSerializer(statuses, many=True)
    return Response(serializer.data)


# Get all programs of study
@api_view(['GET'])
def all_program_of_study(request):
    # query the database for all programs of study
    programs = ProgramOfStudy.objects.all()
    serializer = ProgramOfStudySerializer(programs, many=True)
    return Response(serializer.data)

# Get all departments
@api_view(['GET'])
def all_departments(request):
    # query the database for all departments
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)

# Get all positions
@api_view(['GET'])
def all_positions(request):
    # query the database for all positions
    positions = Position.objects.all()
    serializer = PositionSerializer(positions, many=True)
    return Response(serializer.data)

# Get all course lectrers
@api_view(['GET'])
def all_course_schedule_lecturer(request):
    # query the database for all course schedules lecturers
    course_schedule_lecturers = CourseScheduleLecturer.objects.all()
    serializer = CourseScheduleLecturerSerializer(course_schedule_lecturers, many=True)
    return Response(serializer.data)

# Get all course schedules taught by a lecturer
@api_view(['GET'])
def course_schedule_lecturer(request, id):
    # query the database for all course schedules taught by a lecturer
    course_schedule_lecturers = CourseScheduleLecturer.objects.filter(lecturer_id=id)
    serializer = CourseScheduleLecturerSerializer(course_schedule_lecturers, many=True)
    return Response(serializer.data)

# Get all course enrollments
@api_view(['GET'])
def all_course_enrollments(request):
    # query the database for all course enrollments
    course_enrollments = CourseEnrollment.objects.all()
    serializer = CourseEnrollmentSerializer(course_enrollments, many=True)
    return Response(serializer.data)

# Get course enrollment for a course
@api_view(['GET'])
def course_enrollment(request, id):
    # query the database for all course enrollments where the course schedule has a course with an id of the id
    course_enrollments = CourseEnrollment.objects.filter(course_schedule__course_id=id)
    serializer = CourseEnrollmentSerializer(course_enrollments, many=True)
    return Response(serializer.data)

# Login
@api_view(['POST'])
def login(request):
    # query the database for a user with the username and password
    login = User.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')).exists()
    return Response(login)


# Get prerequisites for a course
@api_view(['GET'])
def course_prerequisites(request, id):
    # query the database for all prerequisites for a course
    prerequisites = CoursePrerequisite.objects.filter(course_id=id)
    serializer = CoursePrerequisiteSerializer(prerequisites, many=True)
    return Response(serializer.data)
