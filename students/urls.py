from . import views 
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    #path('search/', views.search, name='search')
    path('<str:student_number>/', views.student_info, name='student_info')
]
