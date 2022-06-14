from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
# Create your views here.


@api_view(['GET'])

def show_details(request):
    students = {
        'name': 'okunzo'
    }

    return Response(students)