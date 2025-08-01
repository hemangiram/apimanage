from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,status
from django.shortcuts import get_object_or_404
from .models import Student,Office
from .serializers import StudentSerializers
from .serializers import OfficeSerializers


class StudentListCreate(generics.ListCreateAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializers


class OfficeListCreate(generics.ListCreateAPIView):
        queryset = Office.objects.all()
        serializer_class = OfficeSerializers


class StudentDetailAPIView(APIView):
      def get(self,request,pk):
         students = get_object_or_404(Student,pk = pk)
         serializers_class =  StudentSerializers(students)
         return Response(serializers_class.data)
      def put(self,request,pk):
            students = get_object_or_404(Student,pk = pk)
            serializers_class = StudentSerializers(students,data=request.data)
            if serializers_class.is_valid():
                  serializers_class.save()
                  return Response(serializers_class.data)
            return Response(status=status.ERROR_404_CONTENT)
      def delete(self,request,pk):
                 students = get_object_or_404(Student,pk = pk)
                 students.delete()       
                 return Response(status=status.HTTP_204_BAD_ON) 
        
