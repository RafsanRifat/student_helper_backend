from django.shortcuts import render

# Create your views here.

#Rest_Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def students(request):
    return Response({"message": "Hi, welcome to our new API"})