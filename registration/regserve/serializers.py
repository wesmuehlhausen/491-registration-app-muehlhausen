from rest_framework import serializers
# from rest_framework.serializers import serializers
from .models import *

# DONT DO THIS pip install python-rest-framework
# DO THIS pip install dejangorestframework

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','firstname', 'lastname', 'idnumber', 'email', 'schoolyear', 'major', 'gpa', 'datecreated', 'datemodified')
        read_only_fields = ('datecreated', 'datemodified')

    def create_student(self, validated_data):
        return Student(**validated_data)