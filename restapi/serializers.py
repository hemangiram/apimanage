from rest_framework import serializers
from .models import Nurse, Patient, Doctor,ImageUpload,FileUpload

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(many=True, queryset=Nurse.objects.all())  

    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'



class ImageUploadSerializer(serializers.ModelSerializer):
         class Meta:
              model = ImageUpload
              fields = ['id', 'title', 'image']



class FileSerializer(serializers.ModelSerializer):
     class Meta:
          model = FileUpload
          fields = '__all__'
          