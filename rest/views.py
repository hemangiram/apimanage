from django.shortcuts import render
from django.shortcuts import  get_object_or_404
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.views import APIView
from .serializers import FruitSerializer
from .models import Fruit
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, filters
from .pagination import CustomPagination  
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView




class ActiveFruitListView(ListAPIView):
    queryset = Fruit.objects.filter(status='active') 
    serializer_class = FruitSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination



class FruitListCreate(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes= [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'name']
    search_fields = ['name', 'quantity']
    pagination_class = CustomPagination

class FruitDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        fruit= get_object_or_404(Fruit,pk=pk)
     

        serializer = FruitSerializer(fruit)
        return Response(serializer.data)
    def put(self,request,pk):
        fruit = get_object_or_404(Fruit,pk=pk)
        serializer = FruitSerializer(fruit, data = request.data)
        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk):
        fruit = get_object_or_404(Fruit,pk=pk)
        fruit.delete()
        print("fdgfgh")
        return Response(status=status.HTTP_204_NO_CONTENT )

    