from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegisterAPI(APIView):
    permission_classes =[AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=201)
        return Response(serializer.errors,status=404)



class LoginAPI(APIView):
    permission_classes =[AllowAny]

    def post(self,request):
       serializer=LoginSerializer(data=request.data)
       if serializer.is_valid():
           user = serializer.validated_data
           token, _ = Token.objects.get_or_create(user=user)
           return Response({'token':token.key})
       return Response(serializer.erros,status=404)
    

class LogoutAPI(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes =[IsAuthenticated]

   def get(self,request):
       request.user.auth_token.delete()
       return Response({'message':'logout the scessfully'})



