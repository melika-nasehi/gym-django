from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course, Session
from .serializers import CourseSerializer, SessionSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.

class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer




