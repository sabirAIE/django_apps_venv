from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

#create a router instance from Default Router
router = DefaultRouter()
#register studentViewSetAPI with Router
#from this Router url we get Read and Write previllages
router.register('studentAPI', studentModelViewSet_API, basename='student')

#from this router URL we get Only Read Permissions
router.register('studenReadOnlyAPI',studentReadOnlyModelView_API, basename='student_read_only')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls),name='studentAPIs')
]