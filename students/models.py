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
    
class Certificate(models.Model):
    
    def __repr__(self):
        return self.student_number + ": " + self.certificate_type + ' ' + self.date_issued
        
    student_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=64)
    date_issued = models.DateField()
    certificate_hash = models.CharField(max_length=64, primary_key=True)