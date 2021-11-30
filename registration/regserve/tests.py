from django.test import TestCase, Client
from .models import *

class DataTest(TestCase):
    def setUp(self):
        student1 = Student.objects.create(
            firstname="First", 
            lastname="Student",
            idnumber=100,
            email="first@student.edu",
            schoolyear="SR",
            major="CS",
            gpa=4.0,)

        student2 = Student.objects.create(
            firstname="Second", 
            lastname="Student",
            idnumber=101,
            email="second@student.edu",
            schoolyear="SR",
            major="ENG",
            gpa=2.0,)

    def test_student(self): 
        student_list = Student.objects.all()
        student = student_list[0]
        print(f'Inside test student: student is {student}')
        self.assertEqual(student.id, 1)
        self.assertEqual(student.full_name, 'First Student')
        self.assertEqual(student.idnumber, 100)


class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'Simple response test: {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello world from django backend")

#Run in command line: py manage.py test

# Create your tests here.
