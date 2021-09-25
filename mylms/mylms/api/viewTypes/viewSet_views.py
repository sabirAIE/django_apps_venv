from .models import studentModel
from .serializers import studentModelSerializer
from rest_framework import viewsets, status
from django.shortcuts import render 
from rest_framework.response import Response

"""
    *   CRUD operations using the Rest Framework View Set
    *   A ViewSet class is simply a type of class-based View, that does not provide any method handlers such 
        as .get() or .post(), and instead provides actions such as .list(), .create(), .update(), 
        .partial_update(), .retrieve(), .destroy()
"""

class studentViewSet_API(viewsets.ViewSet):
    #define List Method to get All data
    def list(self,request):

        students_data = studentModel.objects.all()
        if students_data.count() > 0:
            serial_data = studentModelSerializer(students_data, many=True)
            res = {'status':1, 'message':'Data Found, Retrieving data...', 'data':serial_data.data}
            return Response(res, status = status.HTTP_200_OK)
        else:
            res = {'status':1, 'message':'No data found in the Database',}
            return Response(res, status = status.HTTP_200_OK)


    #define Retrieve Method to get data by PK
    def retrieve(self, request, pk=None):
        if pk is not None:
            student_data = studentModel.objects.filter(pk=pk)
            serial_data = studentModelSerializer(student_data, many=True)
            res = {'status':1, 'message':'Data Found, Retriving...','data':serial_data.data}
            return Response(res, status= status.HTTP_200_OK)
        else:
            res = {'status':0, 'message':'No data Found',}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    #define Create Method to Insert data/POST data
    def create(self,request):
        serial_data = studentModelSerializer(data = request.data)
        #check post data is valid or not
        if serial_data.is_valid():
            serial_data.save()
            res = {'status':1, 'message':'Data has been Saved', 'data':serial_data.data}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res = {'status':0, 'message':serial_data.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
    
    #define Partial_update Method to update partially, Set Partial in serializer True
    def partial_update(self, request,pk=None):
        if pk is not None:
            student_data = studentModel.objects.get(id=pk)
            serial_data = studentModelSerializer(student_data,data=request.data,partial=True)
            if serial_data.is_valid():
                serial_data.save()
                res = {'status':1, 'message':'Partial data successfully updated', 'data':serial_data.data}
                return Response(res, status =status.HTTP_200_OK)
            else:
                res = {'status':0, 'message':serial_data.errors }
                return Response(res, status= status.HTTP_400_BAD_REQUEST)
        else:
            res = {'status':0, 'message':'Invalid request detected! Access denied'}

    #define Update Method to Completly update data
    def update(self, request,pk=None):
        if pk is not None:
            student_data = studentModel.objects.get(id=pk)
            serial_data = studentModelSerializer(student_data, data=request.data)
            if serial_data.is_valid():
                serial_data.save()
                res = {'status':1, 'message':'Update has been successful!', 'data':serial_data.data}
                return Response(res, status=status.HTTP_200_OK)
            else:
                res = {'status':0, 'message':serial_data.errors}
                return Response(res, status=status.HTTP_401_UNAUTHORIZED)
        else:
            res = {'status':0, 'message':'Invalid request detected! Access denied'}
            return Response(res, status=status.HTTP_401_UNAUTHORIZED)

    #define Destroy Method to delete record
    def destroy(self,request,pk=None):
        if pk is not None:
            student_data = studentModel.objects.filter(pk=pk)
            if student_data.count() == 0:
                res = {'status':0, 'message':'No data found to delete'}
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
            else:
                student_data.delete()
                res = {'status':1, 'message':'Detetion has been successfully proccessed',}
                return Response(res, status=status.HTTP_200_OK)
        else:
            res = {'status':0, 'message':'Invalid request detected! Access denied'}
            return Response(res, status=status.HTTP_401_UNAUTHORIZED)

