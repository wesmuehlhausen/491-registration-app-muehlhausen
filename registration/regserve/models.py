from django.db import models
from django.core import validators
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse, reverse_lazy


#Create a model for each student and the data we have on them
class Person(models.Model):

    #Data we have on student
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idnumber = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)

    #Helper to return full name
    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    class Meta: 
        abstract = True

    #Get all values in string
    def __str__(self):
        return f'Person ID: {self.id}: name: {self.full_name}, student id: {self.idnumber}, email: {self.email}, Created: {self.datecreated}, Modified: {self.datemodified}'

#Student Class
class Student(Person):

    #Values for year in school
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    #Values for different majors
    MAJORS = [
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('BUS', 'Business'),
        ('SC', 'Science'),
        ('LAW', 'Law'),
        ('NUR', 'Nursing'),
        ('UND', 'Undecided'),
    ]

    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)
    major = models.CharField(max_length=3, choices=MAJORS)
    gpa = models.FloatField(max_length=4, blank=True)

    def __str__(self):
        return f'Student ID: {self.id}: {super(Student, self).__str__()} - year in school {self.schoolyear}, major: {self.major}, gpa: {self.gpa}'

    def get_absolute_url(self):
        return reverse_lazy('regserve:students')

