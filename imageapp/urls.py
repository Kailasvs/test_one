from django.urls import path
from . views import PhotAPI

urlpatterns = [
    path('',PhotAPI.as_view())
]
