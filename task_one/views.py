from django.shortcuts import render
from . models import Doctors,Hospital
from . serializers import DoctorSerializer,HospitalSerializer,RegisterSerializer,MyTokenObtainPairSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
  

class RegisterAPI(APIView):
    serializer_class=RegisterSerializer
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Succesfully registered'},status=status.HTTP_201_CREATED)

class HospitalViewSet(viewsets.ModelViewSet):
    """
    A viewset for register and edit user instances.
    """
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()
    http_method_names = ['get', 'post', 'put' , 'delete']


class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for register and edit user instances.
    """
    serializer_class = DoctorSerializer
    queryset = Doctors.objects.all()
    http_method_names = ['get', 'post', 'put' , 'delete'] 
    
   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer