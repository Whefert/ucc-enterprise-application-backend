from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class CourseScheduleSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)
    course_section = CourseSectionSerializer(many=False)
    semester = SemesterSerializer(many=False)
    course = CourseSerializer(many=False)
    class Meta:
        model = CourseSchedule
        fields = '__all__'




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

# User serializer
class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    contact_details = ContactDetailsSerializer(many=False)
    title = serializers.CharField(source = 'title.title', read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source = 'position.name', read_only=True)
    user = UserSerializer(many=False)
    department = serializers.CharField(source = 'department.name', read_only=True)
    class Meta:
        model = Staff
        fields = '__all__'

class EnrollmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentStatus
        fields = '__all__'

# Student serializer
class StudentSerializer(serializers.ModelSerializer):
    calculate_gpa = serializers.ReadOnlyField()
    completed_credits = serializers.ReadOnlyField()
    first_name = serializers.CharField(source = 'user.first_name', read_only=True)
    last_name = serializers.CharField(source = 'user.last_name', read_only=True)
    address = serializers.CharField(source = 'user.address.line1', read_only=True)
    personal_email = serializers.CharField(source = 'user.contact_details.email', read_only=True)
    user = UserSerializer(many=False)
    advisor = StaffSerializer(many=False)
    enrollment_status = serializers.CharField(source = 'enrollment_status.status', read_only=True)
    program_of_study = serializers.CharField(source = 'program_of_study.name', read_only=True)
    degree_level = serializers.CharField(source = 'program_of_study.degree_level', read_only=True)

    class Meta:
        model = Student
        fields = "__all__"

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    final_grade = serializers.ReadOnlyField()
    calculate_gpa = serializers.ReadOnlyField(default='0.0', initial='0.0')
    letter_grade = serializers.ReadOnlyField()
    quality_points = serializers.ReadOnlyField()
    student = StudentSerializer(many=False)
    
    course_schedule = CourseScheduleSerializer(many=False)
    class Meta:
        model = CourseEnrollment
        fields = '__all__'


# Program of study serializer
class ProgramOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramOfStudy
        fields = "__all__"

# Course schedule lecturer serializer
class CourseScheduleLecturerSerializer(serializers.ModelSerializer):
    course_schedule = CourseScheduleSerializer(many=False)
    lecturer = StaffSerializer(many=False)
    class Meta:
        model = CourseScheduleLecturer
        fields = "__all__"


# Coure prerequisite serializer
class CoursePrerequisiteSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False)
    prerequisite = CourseSerializer(many=False)
    class Meta:
        model = CoursePrerequisite
        fields = "__all__"