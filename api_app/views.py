from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from api_app.serializers import ProjectSerializer, ProfileSerializer
from awwwards_app.models import Project
from users.models import Profile
# Create your views here.



class ProjectAPIView(APIView):
    def get(self, request, format = None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileAPIView(APIView):
    def get(self, request, format = None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)