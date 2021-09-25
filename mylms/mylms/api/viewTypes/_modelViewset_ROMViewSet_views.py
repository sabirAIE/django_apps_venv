from .models import studentModel
from .serializers import studentModelSerializer
from rest_framework import viewsets
"""
@ Performing CRUD operations using Model view set, Model view set inherits from Generic API Views
only this much of code is performs all List, Create, Retrieve, Put, Patch, and Delete oprations 
"""
class studentModelViewSet_API(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

"""
@ There are another viewSet. Model Viewset which is read only means we will the only List and Retrieve
functionality from the ReadOnlyModelView
"""

class studentReadOnlyModelView_API(viewsets.ReadOnlyModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer