from django.db.models import base
from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

route = DefaultRouter()

#register the router here
route.register('getStudentThrottle_api',getStudentThrottleLimit_API,basename='student_throttle_api')
route.register('getStudentsThrottleAuthOnly_API',getStudentsThrottleAuthOnly_API,basename='student_throttle_readOnly_api')
app_name = 'api'

urlpatterns = [
    path('studentApiViewAllOperations_API',StudentDetailsClass.as_view(),name='get_students_all_api'),
    path('',include(route.urls),name='modelView_router')
]
