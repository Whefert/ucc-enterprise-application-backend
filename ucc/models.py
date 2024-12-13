from django.db import models

#create a model for degree level
class DegreeLevel(models.Model):
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "degree_level"

#create a model for a program of study
class ProgramOfStudy(models.Model):
    name = models.CharField(max_length=50)
    degree_level = models.ForeignKey(DegreeLevel, related_name='programs_of_study', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "program_of_study"
       
#create a model for contact details
class ContactDetails(models.Model):
    email = models.EmailField(max_length=50)
    mobile_phone = models.CharField(max_length=12)
    home_phone = models.CharField(max_length=12)
    work_number = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "contact_details"

#create a model for address
class Address(models.Model):
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    cityTown = models.CharField(max_length=50)
    parish = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "address"

# create a model for a title
class Title(models.Model):
    title = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "title"

# create a model for a next of kin
class NextOfKin(models.Model):
    user = models.ForeignKey('User', related_name='next_of_kin', on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "next_of_kin"

#create a model for a user
class User(models.Model):
    title = models.ForeignKey(Title, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, related_name='users', on_delete=models.CASCADE)
    contact_details = models.ForeignKey(ContactDetails, related_name='users', on_delete=models.CASCADE)
    next_of_kin0 = models.ForeignKey(NextOfKin, related_name='users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "user"

# create a model for a student
class Student(models.Model):
    user = models.ForeignKey(User, related_name='students', on_delete=models.CASCADE)
    program_of_study = models.ForeignKey('ProgramOfStudy', related_name='students', on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    ucc_email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "student"

# create a model for a course
class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    credits = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course"

# create a model for a department   
class Department(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "department"

#create a model for login credentials
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "login"

#create a model for a position
class Position(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "position"

# create a model for a staff
class Staff(models.Model):
    user = models.ForeignKey(User, related_name='staff', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='staff', on_delete=models.CASCADE)
    login = models.ForeignKey(Login, related_name='staff', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='staff', on_delete=models.CASCADE)
    ucc_email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "staff"

# create a model for courseSection
class CourseSection(models.Model):
    courseSection = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_section"

#create a model for location
class Location(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "location"

# create a model for semester
class Semester(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "semester"

# create a courseSchedule model
class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, related_name='course_schedules', on_delete=models.CASCADE)
    course_section = models.ForeignKey(CourseSection, related_name='course_schedules', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='course_schedules', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name='course_schedules', on_delete=models.CASCADE)
    year = models.IntegerField()
    day1 = models.CharField(max_length=10)
    day2 = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_schedule"

# create a model for courseScheduleLecturers
class CourseScheduleLecturer(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, related_name='course_schedule_lecturers', on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, related_name='course_schedule_lecturers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_schedule_lecturer"


#create a model for courseEnrollment
class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, related_name='course_enrollments', on_delete=models.CASCADE)
    course_schedule = models.ForeignKey(CourseSchedule, related_name='course_enrollments', on_delete=models.CASCADE)
    courseWorkGrade = models.DecimalField(max_digits=3, decimal_places=2)
    finalExamProjectGrade = models.DecimalField(max_digits=3, decimal_places=2)
    finalGrade = models.DecimalField(max_digits=3, decimal_places=2)
    letterGrade = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_enrollment"

#create a model for coursePrerequisite
class CoursePrerequisite(models.Model):
    course = models.ForeignKey(Course, related_name='course_prerequisites', on_delete=models.CASCADE)
    prerequisite = models.ForeignKey(Course, related_name='course_prerequisites0', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_prerequisite"