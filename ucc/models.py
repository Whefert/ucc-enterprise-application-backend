from django.db import models


class Test (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "test"


#create a model for address
class Address(models.Model):
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    cityTown = models.CharField(max_length=50)
    parish = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "address"


# create a model for a student
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.CharField(max_length=2)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# create a model for a teacher
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# create a model for a course
class Course(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

