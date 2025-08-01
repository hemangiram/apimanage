from rest_framework import generics,status,filters
from .models import Nurse, Patient, Doctor,FileUpload
from .serializers import NurseSerializer, PatientSerializer, DoctorSerializer,ImageUploadSerializer,FileSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .pagination import CustomPagination

# Nurse Views
class NurseListCreate(generics.ListCreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name','detail']
    search_fields = ['name', 'detail']
    pagination_class = CustomPagination
class NurseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [AllowAny]

# Patient Views
class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]



class ImageUploadAPIView(APIView):
   permission_classes = [AllowAny]
   parser_class =[MultiPartParser,FormParser]

   def post(self,request,formate=None):
       print("request",request.data)
       serialilizer = ImageUploadSerializer(data = request.data)
       if serialilizer.is_valid():
           serialilizer.save()
           print("serializer save")
           return Response(serialilizer.data, status=status.HTTP_201_CREATED)
       print("serializer error",serialilizer.errors)
       return Response(serialilizer.errors,status=status.HTTP_400_BAD_REQUEST)
   


class FileUploadAPIView(APIView): 
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser] 

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'File uploaded successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)