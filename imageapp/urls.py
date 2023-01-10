from django.urls import path,include
from . views import PhotoViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'',PhotoViewset)


urlpatterns = [
     path('',include(router.urls)),
]
