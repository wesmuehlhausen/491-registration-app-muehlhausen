from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from rest_framework import generics
from django.views.generic import ListView, CreateView

#Get an http response
def index(request):
    return HttpResponse("Hello world from django backend")

#Student list view class
class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Create form for student list
class StudentListForm(ListView):
    model = Student

#Create form for student
class StudentCreateForm(CreateView, ListView):
    model = Student
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']
