from . import views 
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('validate_hash/', views.validateHash, name='validate_hash'),
    #path('search/', views.search, name='search')
    path('search/', views.search, name='search'),
    path('view-certificate/', views.viewCert, name='viewCert'),
    path('certificate/<str:certificate_hash>/', views.viewCertInfo, name='viewCertInfo'),
    path('<str:student_number>/', views.student_info, name='student_info'),
    
    
    
]
