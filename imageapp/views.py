from django.shortcuts import render
from .serializers import Photoserializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Photo
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class PhotoViewset(ModelViewSet):
    """
    A viewset for register and edit user instances.
    """
    serializer_class = Photoserializer
    queryset = Photo.objects.all()
    http_method_names = ['get', 'post', 'put' , 'delete'] 
    def create(self,request):
        serializer=Photoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"sucess"})
        return Response(serializer.errors)
    
    def list(self,request):
            photo=Photo.objects.all()
            serializer=Photoserializer(photo,many=True)
            for s in serializer.data :
                s['image']=settings.HOST_ADDRESS  +  s['image']
            return Response(serializer.data)