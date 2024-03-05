from rest_framework import serializers
from app.models import *


class StudentModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        