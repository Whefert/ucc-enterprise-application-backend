from django.db import models

#create a model for degree level
class DegreeLevel(models.Model):
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level

    class Meta:
        db_table = "degree_level"

#create a model for a program of study
class ProgramOfStudy(models.Model):
    name = models.CharField(max_length=50)
    degree_level = models.ForeignKey(DegreeLevel, related_name='programs_of_study', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.degree_level.level

    class Meta:
        db_table = "program_of_study"
       
#create a model for contact details
class ContactDetails(models.Model):
    email = models.EmailField(max_length=50)
    mobile_phone = models.CharField(max_length=12)
    home_phone = models.CharField(max_length=12, blank=True, null=True)
    work_number = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email + " " + self.mobile_phone

    class Meta:
        db_table = "contact_details"

#create a model for address
class Address(models.Model):
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50, blank=True, null=True)
    cityTown = models.CharField(max_length=50)
    parish = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line1 + ", " + self.cityTown + ", " + self.parish + ", " + self.country

    class Meta:
        db_table = "address"

# create a model for a title
class Title(models.Model):
    title = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "title"

# create a model for a next of kin
class NextOfKin(models.Model):
    # id of the relative/next of kin
    user = models.ForeignKey('User', related_name='next_of_kin', on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # student or member of staff
    kin= models.ForeignKey('User', related_name='next_of_kin0', on_delete=models.CASCADE)  

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.relationship + " to " + self.kin.first_name + " " + self.kin.last_name

    class Meta:
        db_table = "next_of_kin"

#create a model for a user
class User(models.Model):
    title = models.ForeignKey(Title, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    contact_details = models.ForeignKey(ContactDetails, related_name='users', on_delete=models.SET_NULL, blank=True, null=True) 
    next_of_kin1 = models.ForeignKey(NextOfKin, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        db_table = "user"

# create a model for enrollment status
class EnrollmentStatus(models.Model):
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        db_table = "enrollment_status"



# create a model for a course
class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    credits = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + " - " + self.title

    class Meta:
        db_table = "course"



# create a model for a department   
class Department(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "department"

#create a model for login credentials
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + " " + self.password

    class Meta:
        db_table = "login"

#create a model for a position
class Position(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "position"

# create a model for a staff
class Staff(models.Model):
    user = models.ForeignKey(User, related_name='staff', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='staff', on_delete=models.SET_NULL, blank=True, null=True)
    login = models.ForeignKey(Login, related_name='staff', on_delete=models.SET_NULL, blank=True, null=True)
    position = models.ForeignKey(Position, related_name='staff', on_delete=models.SET_NULL, blank=True, null=True)
    ucc_email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+ " - " + self.user.first_name + " " + self.user.last_name

    class Meta:
        db_table = "staff"


# create a model for a student
class Student(models.Model):
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    program_of_study = models.ForeignKey('ProgramOfStudy', related_name='students', on_delete=models.SET_NULL, blank=True, null=True)   
    ucc_email = models.EmailField(max_length=50)
    enrollment_status = models.ForeignKey(EnrollmentStatus, related_name='students', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    advisor = models.ForeignKey('Staff', related_name='students', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id) + " - "+ self.user.first_name + " " + self.user.last_name
    
    # calculated field for the students gpa
    @property
    def calculate_gpa(self):
        total = 0
        count = 0
        # find and courses the student is enrolled in
        student_courses = CourseEnrollment.objects.filter(student=self)

        # if no courses are found return 0
        if not student_courses:
            return 0

        # loop through the courses and calculate the gpa
        for course in student_courses:
            total += course.quality_points
            count += 1
        return total/count
    
    def completed_credits(self):
        total = 0
        student_courses = CourseEnrollment.objects.filter(student=self)
        for course in student_courses:
            total += course.course_schedule.course.credits
        return total


    class Meta:
        db_table = "student"



# create a model for courseSection
class CourseSection(models.Model):
    courseSection = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.courseSection

    class Meta:
        db_table = "course_section"

#create a model for location
class Location(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "location"

# create a model for semester
class Semester(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "semester"

# create a courseSchedule model
class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, related_name='course_schedules', on_delete=models.CASCADE)
    course_section = models.ForeignKey(CourseSection, related_name='course_schedules', on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, related_name='course_schedules', on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ForeignKey(Semester, related_name='course_schedules', on_delete=models.SET_NULL, blank=True, null=True)
    year = models.IntegerField()
    day1 = models.CharField(max_length=10)
    day2 = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.code + " - " + self.course.title + " - " + self.location.name + " - " + self.semester.name + " - " + str(self.year)

    class Meta:
        db_table = "course_schedule"

# create a model for courseScheduleLecturers
class CourseScheduleLecturer(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, related_name='course_schedule_lecturers', on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Staff, related_name='course_schedule_lecturers', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_schedule.course.code + " - " + self.course_schedule.course.title + " - " + self.lecturer.user.first_name + " " + self.lecturer.user.last_name + " - " + self.course_schedule.location.name + " - " + self.course_schedule.semester.name + " - " + str(self.course_schedule.year)

    class Meta:
        db_table = "course_schedule_lecturer"


#create a model for courseEnrollment
class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, related_name='course_enrollments', on_delete=models.CASCADE)
    course_schedule = models.ForeignKey(CourseSchedule, related_name='course_enrollments', on_delete=models.CASCADE)
    courseWorkGrade =models.FloatField(default=50)
    finalExamProjectGrade = models.FloatField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.user.first_name + " " + self.student.user.last_name + " - " + self.course_schedule.course.code + " - " + self.course_schedule.course.title + " - " + self.course_schedule.location.name + " - " + self.course_schedule.semester.name + " - " + str(self.course_schedule.year)

    @property
    def calculate_gpa(self):
  
        if self.final_grade >= 90:
            return 4.0
        elif self.final_grade >= 80:
            return 3.67
        elif self.final_grade >= 75:
            return 3.50
        elif self.final_grade >= 65:
            return 3.0
        elif self.final_grade >= 60:
            return 2.67
        elif self.final_grade >= 55:
            return 2.33
        elif self.final_grade >= 50:
            return 2.00
        elif self.final_grade >= 40:
            return 1.67
        else:
            return 0.0

    # calculate field for final grade
    @property
    def final_grade(self):
         return self.courseWorkGrade*.6 + self.finalExamProjectGrade*.4
    
    # calculate letter grade
    @property   
    def letter_grade (self):
       
        if self.final_grade >= 90:
            return "A"
        elif self.final_grade >= 80:
            return "A-"
        elif self.final_grade >= 75:
            return "B+"
        elif self.final_grade >= 65:
            return "B"
        elif self.final_grade >= 60:
            return "B-"
        elif self.final_grade >= 55:
            return "C+"
        elif self.final_grade >= 50:
            return "C"
        elif self.final_grade >= 40:
            return "D"
        else:
            return "F"

    @property
    def quality_points(self):

        if self.final_grade >= 90:
            return 4.0
        elif self.final_grade >= 80:
            return 3.67
        elif self.final_grade >= 75:
            return 3.50
        elif self.final_grade >= 65:
            return 3.0
        elif self.final_grade >= 60:
            return 2.67
        elif self.final_grade >= 55:
            return 2.33
        elif self.final_grade >= 50:
            return 2.00
        elif self.final_grade >= 40:
            return 1.67
        else:
            return 0.0


    class Meta:
        db_table = "course_enrollment"

#create a model for coursePrerequisite
class CoursePrerequisite(models.Model):
    course = models.ForeignKey(Course, related_name='course_prerequisites', on_delete=models.CASCADE)
    prerequisite = models.ForeignKey(Course, related_name='course_prerequisites0', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_prerequisite"