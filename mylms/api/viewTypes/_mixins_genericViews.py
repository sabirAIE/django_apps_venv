
from abc import abstractclassmethod
from .models import StudentModel
from .serializers import StudentModelSerializer

from rest_framework.generics import GenericAPIView
from rest_framework import mixins

#CRUD GPPPD Operations using REST Framework Mixins we will be using these Functionalities in our
"""
    * Get all students GET METHOD
    * Get students by id GET METHOD
    * Save or Insert post data using POST METHOD
    * Update a Studenent Infromation PUT METHOD supports both PATCH and PUT
    * Delete a stduent information DELETE METHOD
"""
#get all students and Save a students
class StudentListCreateAPI(GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    #Get all Students
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    #Create Student details in data base
    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)
    


class StudentOperationsAPI(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    #get student by id PK
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    #update students put or patch both works
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #delete a stduent data
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    