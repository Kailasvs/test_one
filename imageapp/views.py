from django.shortcuts import render
from .serializers import Photoserializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Photo
# Create your views here.


class PhotAPI(APIView):
    serializer_class=Photoserializer
    def post(self,request):
        serializer=Photoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"sucess"})
        return Response(serializer.errors)
    
    def get(self,request):
            photo=Photo.objects.all()
            serializer=Photoserializer(photo,many=True)
            return Response(serializer.data)