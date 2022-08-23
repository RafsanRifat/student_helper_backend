from django.contrib import admin
from django.urls import path
from .views import allurls, TeacherSignupView, StudentSignupView, TeacherList, StudentList

urlpatterns = [
    path('api/students', allurls, name='allurls'),
    path('api/teacher/signup', TeacherSignupView.as_view(), name='teachersignup'),
    path('api/teacher/list', TeacherList.as_view(), name='teacherlist'),
    path('api/student/signup', StudentSignupView.as_view(), name='studentsignup'),
    path('api/student/list', StudentList.as_view(), name='studentlist'),
]
