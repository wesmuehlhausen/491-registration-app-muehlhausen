from rest_framework import serializers
from .models import *

#Class for student serializer. Includes student fields and other fields
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','firstname', 'lastname', 'idnumber', 'email', 'schoolyear', 'major', 'gpa', 'datecreated', 'datemodified')
        read_only_fields = ('datecreated', 'datemodified')

    def create_student(self, validated_data):
        return Student(**validated_data)