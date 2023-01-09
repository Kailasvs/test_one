from rest_framework import serializers
from . models import Hospital,Doctors



class HospitalSerializer(serializers.ModelSerializer):
    class Meta :
        model = Hospital
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    fk_hospital = HospitalSerializer(read_only=True)
   
    
    class Meta:
        model = Doctors
        fields = '__all__'


    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     if rep['fk_hospital']:
    #         rep['fk_hospital'] = Hospital.objects.filter(id=rep['fk_hospital']).values('id','name','address','description','location')
        
    #     return rep