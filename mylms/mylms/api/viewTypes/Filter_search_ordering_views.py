from .models import studentModel
from .serializers import studentModelSerializer

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, filterset
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

"""
@ In this section we going to implement the different types of 
@ Filters,
@ Searches and 
@ Ordering- as name suggest ordering Alphabetically or Numerically ASC and DESC order
    note: (-) minus is used here for decending ordering of data

@ Here we are using the generic ListApiView and adding a simple or generic filter function. We
    need to use the django-filter for advance filtering. To acomplish this we are going to create a 
    another function based api end point
"""
class getStudentListByLastName(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    def get_queryset(self):
        user = self.request.user
        return studentModel.objects.filter(createdBy=user)
    
"""
# this class based view inherits from ListAPIView and provides additional functionality also
# here we are using DjangoFilterBackend to filter data in the list view. We imoprt from
    #django_filters a third party library
"""
class getStudentFilterList_API(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['firstName','lastName']

"""
# Let's Create a class bases API using generic ListAPIView implementing  Search this api 
    is limited to admin user only.
"""
class getStudentSearchList_API(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter]
    search_fields = ['lastName','firstName','email']


"""
# Let's create a class based api using generic ListAPIView and apply filter_backend- 
    OrderingFilter this is open for all user type.
"""
class getStudentListOrder_API(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    filter_backends = [OrderingFilter]
    # ordering_fields = ['id','firstName']
    ordering_fields = '__all__'