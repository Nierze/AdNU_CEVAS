from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    
    def __str__(self):
        return self.student_number + ": " + self.first_name + ' ' + self.middle_name[0] + '. ' + self.last_name
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=11)
    course = models.CharField(max_length=50)
    year_level = models.IntegerField()
    section = models.CharField(max_length=10)
    student_number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(r'^CO\d{4}-\d{5}$', message='Invalid student number format')], primary_key=True)
    
# sampleStudent = Student(first_name='Juan', last_name='Dela Cruz', middle_name='Santos', age=20, address='Purok 1, Brgy. San Isidro, Iriga City', email='jd@gmail.com', contact_number='09123456789', course='BSIT', year_level=1, section='A', student_number='CO2021-12345')