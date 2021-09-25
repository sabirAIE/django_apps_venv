from django.urls import path
from .views import *


app_name = 'api'

urlpatterns = [
    path('studentList/', studentsList_API.as_view() ), #will be used for POST, PUT, PATCH, DELETE
    path('studentCreateAPI/',  studentCreate_API.as_view()),
    path('studentListCreate/', studentListCreate_API.as_view()),
    path('studentUpdateRetriveDelete/<int:pk>/', studentRetriveUpdateDelete_API.as_view()),
]