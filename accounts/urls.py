from django.contrib import admin
from django.urls import path
from .views import students, TeacherSignupView, StudentSignupView

urlpatterns = [
    path('api/students', students, name='students'),
    path('api/teacher/signup', TeacherSignupView.as_view(), name='teachersignup'),
    path('api/student/signup', StudentSignupView.as_view(), name='studentsignup'),
]
