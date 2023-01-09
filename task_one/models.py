from django.db import models

# Create your models here.



class Hospital(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True)
    location=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    

class Doctors(models.Model):
    name = models.CharField(max_length=1000)
    experience =  models.IntegerField(null=True)
    fk_hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='hospital',null=True)
    biography=models.TextField(null=True)
    education=  models.CharField(max_length=1000,null=True)
    
    def __str__(self):
        return self.name