from django.urls import path, include
from .views import *
app_name = 'api'

urlpatterns = [
    path('getStudentListByLastName_api/',getStudentListByLastName.as_view(), name='getStudents_bylastName_api'),
    path('getStudentListFilter_API/',getStudentFilterList_API.as_view(),name='getStudentFilter_api'),
    path('getStudentListSearch_API/', getStudentSearchList_API.as_view(),name='getStudents_searc_api'),
    path('getStudentListOrder_API/',getStudentListOrder_API.as_view(),name='getStudent_order_api')
]
