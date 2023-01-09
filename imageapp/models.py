from django.db import models
import uuid
# Create your models here.
from django.utils.translation import gettext_lazy as _
 
from . fields import WEBPField
 
 
def image_folder(instance, filename):
    return 'photos/{}.webp'.format(uuid.uuid4().hex)
 
 
class Photo(models.Model):
  
    name=models.CharField(max_length=50,null=True)
    image = WEBPField(
        verbose_name=_('Image'),
        upload_to=image_folder,
       
    )