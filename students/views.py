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
    
    return render(request, 'User-Page.html', contexts)


def student_info(request, student_number):
    print(request)
    temp = Student.objects.get(student_number=student_number)
    contexts = {
        'name': str(temp.first_name + ' ' + temp.middle_name[0] + '. ' + temp.last_name),
        'course' : temp.course,
        'student_id' : temp.student_number,
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
    return render(request, 'View-Certification-Page.html', contexts)  

def search(request):
    if request.method == 'GET':  
        search_query = request.GET.get('search')  # Get the student ID from the query string
        if search_query:
            try:
                #######################################################
                contexts = {'certificate_boxes':[]}
                temp = Student.objects.get(student_number=search_query)
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
                
                return render(request, 'Search-Page.html', contexts)
                    
                ######################################################
            
            except Student.DoesNotExist:
                # Handle the case where the student doesn't exist
                return render(request, 'Search-Page.html', {'error_message': 'Student not found'})
        else:
            return render(request, 'Search-Page.html')  # No search query provided
    else:
        return HttpResponse('Invalid request method') 
    
    
def viewCert(request):
    print(request)
    temp = Student.objects.get(student_number='CO2021-54321')
    contexts = {'name' :  str(temp.first_name + ' ' + temp.middle_name[0] + '. ' + temp.last_name), 'certificate_boxes': []}
    
    certificates = Certificate.objects.filter(student_number=temp.student_number)
    for cert in certificates:
        certificate_box = render(request, 'certificateBox.html', {
            'certificate_name': cert.certificate_name,
            'date_issued': cert.date_issued,
            'certificate_hash': cert.certificate_hash,
        })

        # Extract and append the rendered HTML content
        contexts['certificate_boxes'].append(certificate_box.content.decode()) 

        # Print certificate name (for debugging if needed)
        print(cert.certificate_name)
    return render(request, 'View-Certification-Page.html', contexts)


def viewCertInfo(request, certificate_hash):
    print(request)
    temp = Certificate.objects.get(certificate_hash=certificate_hash)
    temp2 = Student.objects.get(student_number=temp.student_number.student_number)
    contexts = {'certificate_name' : temp.certificate_name,
                'date_issued' : temp.date_issued,
                'certificate_hash' : temp.certificate_hash,
                'name' : str(temp2.first_name + ' ' + temp2.middle_name[0] + '. ' + temp2.last_name),
                }
    
    return render(request, 'Certificate-Page.html', contexts)
    
        
def validateHash(request):
    if request.method == 'GET':
        search_query = request.GET.get('validate_hash')  # Use a generic name for the query parameter
        if search_query:
            try:
                cert = Certificate.objects.get(certificate_hash=search_query)
                print(search_query)
                return render(request, 'Validate-Page.html', {'Result': 'Certificate is valid'})
            except Certificate.DoesNotExist:
                return render(request, 'Validate-Page.html', {'Result': 'Certificate not valid'})
        else:
            return render(request, 'Validate-Page.html') 
    else:
        return HttpResponse('Invalid request method') 
    
        
    
    