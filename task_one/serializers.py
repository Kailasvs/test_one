from rest_framework import serializers
from . models import Hospital,Doctors
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



User=get_user_model()

class HospitalSerializer(serializers.ModelSerializer):
    class Meta :
        model = Hospital
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    # fk_hospital = HospitalSerializer(read_only=True)
   
    
    class Meta:
        model = Doctors
        fields = '__all__'


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if rep['fk_hospital']:
            rep['fk_hospital'] = Hospital.objects.filter(id=rep['fk_hospital']).values('id','name','address','description','location')
        
        return rep

class RegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['username','password']

    def save(self):
            reg=User(
                    username=self.validated_data['username'],
                   
                )
            
            password=self.validated_data['password']
            reg.set_password(password)
            reg.save()
            return reg

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['userid']=self.user.id
        data['username'] = self.user.username
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        
       
        return data