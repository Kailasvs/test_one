from . views import HospitalViewSet,DoctorViewSet,RegisterAPI,MyTokenObtainPairView
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
router=DefaultRouter()
router.register(r'hospital',HospitalViewSet)
router.register(r'doctor',DoctorViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterAPI.as_view()),
    path('login/',
         MyTokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
   
    
]

