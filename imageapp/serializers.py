from rest_framework import serializers
from . models import Photo


class Photoserializer(serializers.ModelSerializer):
    class Meta :
        model = Photo
        fields='__all__'