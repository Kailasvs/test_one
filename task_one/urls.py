from . views import HospitalViewSet,DoctorViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'hospital',HospitalViewSet)
router.register(r'doctor',DoctorViewSet)

urlpatterns = [
    path('',include(router.urls))
]
