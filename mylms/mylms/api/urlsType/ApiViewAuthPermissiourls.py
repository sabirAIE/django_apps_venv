from django.urls import path,include
from .views import *

app_name = 'api'

urlpatterns = [
    path('studentGetDetails_API',StudentDetail,name='studentDetails_API'),
    path('studentGetDetails_API/<int:pk>/',StudentDetail,name='studentDetails_API'),
    path('studentOperations_API/',AddNewStudent, name='studentOperations_API'),
]
