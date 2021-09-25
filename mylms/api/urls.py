from django.urls import base, path,include
from rest_framework import routers 
from .views import *
from rest_framework.routers import DefaultRouter
app_name = 'api'


router = DefaultRouter()
router.register('singerInformation_API',singerInformation_API,basename='singer_information_api')
router.register('songInformation_API',songInformation_API,basename='song_information_api')

urlpatterns = [
    path('',include(router.urls),name='song_singer_API'), 
]
