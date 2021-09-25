from django.db.models.manager import BaseManager
from .views import *
from django.urls import path, include
#import Router from default Router
from rest_framework.routers import DefaultRouter

#here we create a instance of Default Router Class
router = DefaultRouter()
#Now have to register a router to interact with our views
router.register('studentAPI', studentModelViewSet_API, basename='student_api')
router.register('studenReadAPI',studentReadOnlyViewSet, basename='studentRead_api')
router.register('studentCustomPermissionAPI',studentModelViewCustomPermission_API,basename='studentCustom_api')

app_name = 'api'

urlpatterns = [
    path('',include(router.urls),name='student_api'),
    
]
