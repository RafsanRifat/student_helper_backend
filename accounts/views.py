from django.shortcuts import render

# Create your views here.

# Rest_Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from .serializers import TeacherSignupSerializer, UserSerializer, TeacherSignupSerializer2, StudentSignupSerializer, \
    StudentSignupSerializer2
from .models import Teacher, Student
from .permissions import IsTeacherUser


@api_view(['GET'])
def allurls(request):
    return Response({
        "Teacher List": "https://studenthelperbackend.herokuapp.com/api/teacher/list",
        "Student List": "https://studenthelperbackend.herokuapp.com/api/student/list",
        "Teacher Signup": "https://studenthelperbackend.herokuapp.com/api/teacher/signup",
        "Student Signup": "https://studenthelperbackend.herokuapp.com/api/student/signup",
    })


# Teacher SignUo view
class TeacherSignupView(generics.GenericAPIView):
    serializer_class = TeacherSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        username = user.username
        teacher = Teacher.objects.get(user__username=username)
        institute = teacher.institute_name
        print(institute)
        print(teacher)
        serializer2 = TeacherSignupSerializer2(teacher)

        return Response({
            # "teacher": UserSerializer(user, context=self.get_serializer_context()).data,
            "teacher": serializer2.data,
            "message": "account created successfully",
        })


# Student signup view

class StudentSignupView(generics.GenericAPIView):
    serializer_class = StudentSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        username = user.username
        student = Student.objects.get(user__username=username)
        Studentextrainfo = StudentSignupSerializer2(student)
        return Response({
            # "student_basic_info": UserSerializer(user, context=self.get_serializer_context()).data,
            "student": Studentextrainfo.data,
            "message": "account created successfully"
        })


# Teacher List (only view)
class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSignupSerializer2


# Teacher List (only view)
class StudentList(generics.ListAPIView):
    # queryset = Student.objects.all()
    serializer_class = StudentSignupSerializer2

    def get_queryset(self):
        students = Student.objects.all()
        return students
