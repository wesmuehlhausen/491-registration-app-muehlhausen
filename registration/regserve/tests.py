from django.test import TestCase, Client
from .serializers import StudentSerializer
from .models import *
import io
from rest_framework.parsers import JSONParser

#Tests
class DataTest(TestCase):
    def setUp(self):
        #Test data for student 1
        student1 = Student.objects.create(
            firstname="First", 
            lastname="Student",
            idnumber=100,
            email="first@student.edu",
            schoolyear="SR",
            major="CS",
            gpa=4.0,)

        #Test data for student 2
        student2 = Student.objects.create(
            firstname="Wesley", 
            lastname="Muehlhausen",
            idnumber=101,
            email="wmuehlhausen@zagmail.gonzaga.edu",
            schoolyear="SR",
            major="ENG",
            gpa=2.0,)
        self.test_client = Client()

    #Method for testing api including: api response, api response content, status, response stream, 
    def test_student_api(self):
        students_response = self.test_client.get('/regserve/data/students/')
        print(f'\nTEST_STUDENT_API: api response {students_response} and the status is {students_response.status_code}')
        self.assertEqual(students_response.status_code, 200)
        print(f'\nTEST_STUDENT_API: api response content is: {students_response.content}')
        student_stream = io.BytesIO(students_response.content)
        print(f'\nTEST_STUDENT_API: api response stream is: {student_stream}')
        student_data = JSONParser().parse(student_stream)
        first_student_data = student_data[0]
        print(f'\nTEST_STUDENT_API: api response data is: {first_student_data} and its id is {first_student_data["id"]}')
        first_student_db = Student.objects.get(id=first_student_data['id'])
        print(f'\nTEST_STUDENT_API: student object from database is: {first_student_db}')
        #Test Student Serializer
        first_student_serializer = StudentSerializer(first_student_db , data=first_student_data)
        print(f'\nTEST_STUDENT_API: respones serializer: {first_student_serializer}')
        print(f'\nTEST_STUDENT_API: respones serializer validity is: {first_student_serializer.is_valid()}')
        print(f'\nTEST_STUDENT_API: respones serializer valid data: {first_student_serializer.validated_data}')
        first_student_api = first_student_serializer.save()
        print(f'\nTEST_STUDENT_API: api response object is : {first_student_api}')
        self.assertEqual(first_student_db, first_student_api)

    #Method for testing it
    def test_student(self): 
        student_list = Student.objects.all()
        student = student_list[0]
        print(f'\nInside test student: student is {student}')
        self.assertEqual(student.id, 1)
        self.assertEqual(student.full_name, 'First Student')
        self.assertEqual(student.idnumber, 100)

#Simple test
class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'\nSimple response test: {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello world from django backend")

