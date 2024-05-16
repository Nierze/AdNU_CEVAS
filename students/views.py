from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student

# Create your views here.
def index(request):
    print(request)
    temp = Student.objects.get(student_number='CO2021-54321')
    contexts = {'name' :  str(temp.first_name + ' ' + temp.middle_name[0] + '. ' + temp.last_name),
                'course' : temp.course,
                'student_id' : temp.student_number
                }
    
    return render(request, 'info.html', contexts)


def student_info(request, student_number):
    print(request)
    # 'CO2021-54321'
    temp = Student.objects.get(student_number=student_number)
    contexts = {'name' :  str(temp.first_name + ' ' + temp.middle_name[0] + '. ' + temp.last_name),
                'course' : temp.course,
                'student_id' : temp.student_number
                }
    
    return render(request, 'info.html', contexts)