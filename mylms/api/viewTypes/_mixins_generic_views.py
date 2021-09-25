
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
#get all students 
class studentDetailsListClass(GenericAPIView, mixins.ListModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

#Create Student details in data base
class studentDetailsCreateClass(GenericAPIView, mixins.CreateModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

#get student by id PK
class studentDetailsRetriveClass(GenericAPIView, mixins.RetrieveModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)


#update students put or patch both works
class studentDetailsUpdateClass(GenericAPIView, mixins.UpdateModelMixin):
    queryset = StudentModel
    serializer_class = StudentModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#delete a stduent data
class studentDetailsDestroyClass(GenericAPIView, mixins.DestroyModelMixin):
    queryset = StudentModel
    serializer_class = StudentModelSerializer

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)