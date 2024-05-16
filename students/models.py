from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    
    def __repr__(self):
        return self.student_number + ": " + self.first_name + ' ' + self.middle_name[0] + '. ' + self.last_name
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    student_number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(r'^CO\d{4}-\d{5}$', message='Invalid student number format')], primary_key=True)
    
    
    
# sampleStudent = Student(first_name='Juan', last_name='Dela Cruz', middle_name='Santos', email='jd@gmail.com, course='BSIT', student_number='CO2021-12345')