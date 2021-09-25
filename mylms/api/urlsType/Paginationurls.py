from django.urls import path, include
from .views import *
app_name = 'api'

urlpatterns = [
    path('getStudentsListPerPage_API/', getStudentListPerPage_API.as_view(),name='get_student_list_pp_api'),
    path('studentListCreate_API/', studentListCreate_API.as_view(), name='get_create_student_api'),
    path('studentListLimitOffsetPagination_API/', studentListLimitOffsetPagination.as_view(),name='get_students_pagination_api'),
    path('studentListCursorPagination_API/',studentListCursorPagination_API.as_view(),name='get_student_cursor_pagination_api'),    
]
