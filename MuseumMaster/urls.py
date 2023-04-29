from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('Meseum-Info', InfoViewSet, basename='Meseum-Info')

urlpatterns = [
    path('', include(router.urls)),
    
]