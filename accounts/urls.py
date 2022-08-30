from django.contrib import admin
from django.urls import path
from .views import api_endpoints, TeacherSignupView, StudentSignupView, TeacherList, StudentList, UserLogoutView, UserDetailView, UserUpdateApiView

urlpatterns = [
    path('', api_endpoints, name='allurls'),
    path('api/teacher/signup', TeacherSignupView.as_view(), name='teachersignup'),
    path('api/teacher/list', TeacherList.as_view(), name='teacherlist'),
    path('api/userdetail/<int:id>', UserDetailView.as_view(), name='userdetail'),
    path('api/userupdate/<pk>', UserUpdateApiView.as_view(), name='userupdate'),
    path('api/student/signup', StudentSignupView.as_view(), name='studentsignup'),
    path('api/student/list', StudentList.as_view(), name='studentlist'),
    path('api/logout', UserLogoutView.as_view(), name='logout'),
]
