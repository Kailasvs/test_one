from django.shortcuts import render
from . models import Doctors,Hospital
from . serializers import DoctorSerializer,HospitalSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.



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
    
    # def list(self, request, *args, **kwargs):
    #    doctors = DoctorSerializer(hospital.hospital.all(), many=True).data
    #    return Response(doctors.data)
