from django.shortcuts import render
from django.http import HttpResponse
from students.models import *

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
    temp = Student.objects.get(student_number=student_number)
    contexts = {
        'name': str(temp.first_name + ' ' + temp.middle_name[0] + '. ' + temp.last_name),
        'course': temp.course,
        'student_id': temp.student_number,
        'certificate_boxes': [],  # Initialize an empty list
    }

    certificates = Certificate.objects.filter(student_number=temp.student_number)
    for cert in certificates:
        certificate_box = render(request, 'certificateBox.html', {
            'certificate_name': cert.certificate_name,
            'date_issued': cert.date_issued,
            'certificate_hash': cert.certificate_hash
        })

        # Extract and append the rendered HTML content
        contexts['certificate_boxes'].append(certificate_box.content.decode()) 

        # Print certificate name (for debugging if needed)
        print(cert.certificate_name)  
    
    # Return the rendered template with the complete context after the loop
    return render(request, 'View-Certificate-Page.html', contexts)  