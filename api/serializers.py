from rest_framework import serializers
from .models import Student
from .models import Office



class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'





class OfficeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'