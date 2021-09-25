from api.models import StudentModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentModelSerializer
from .models import StudentModel
from rest_framework import status

class StudentDetailsClass(APIView):
    
    #define a get function in the Class Based API View
    def get(self, request, pk=None, format= None):
        if pk is not None:
            student_data = StudentModel.objects.filter(pk=pk)
            if student_data.count() == 0:
                res = {'status':0,'message':'No data Found or Invalid params Passed'}
                res_status = status.HTTP_400_BAD_REQUEST
            else:
                serial_data = StudentModelSerializer(student_data,many=True)
                res = {'status':1,'message':'Data Found! Fetching data successfull','data':serial_data.data}
                res_status = status.HTTP_200_OK
            return Response(res, status=res_status)

        student_data = StudentModel.objects.all()
        if student_data.count() == 0:
            res = {'status':0,'message':'No data Found'}
            res_status = status.HTTP_400_BAD_REQUEST
        else:
            serial_data = StudentModelSerializer(student_data,many=True)
            res = {'status':1,'message':'Data Found! Fetching data successfull','data':serial_data.data}
            res_status = status.HTTP_200_OK
        return Response(res)
    
    #define a Post function in the API Class based View
    def post(self, request, format=None):
        post_data = request.data
        serial_data = StudentModelSerializer(data=post_data)
        
        if serial_data.is_valid():
            serial_data.save()
            res = {'status':1,'message':'Data successfully saved','data':serial_data.data}
            res_status = status.HTTP_200_OK
        else:
            res = {'status':0,'message': serial_data.errors,'data':serial_data.data}
            res_status = status.HTTP_400_BAD_REQUEST
        return Response(res, status=res_status)
        
    
    #define a PUT function in the API class based view
    def put(self, request, format=None):
        #check for the Id first
        pk = request.data.get('id')
        student_data = StudentModel.objects.get(id=pk)
        serial_data = StudentModelSerializer(student_data,data=request.data, partial=True)
        if serial_data.is_valid():
            serial_data.save()
            res = {'status':1,'message':'Post data updated successfully','data':serial_data.data}
            res_status = status.HTTP_200_OK
        else:
            res = {'status':0,'message': serial_data.errors,'data':serial_data.data}
            res_status = status.HTTP_400_BAD_REQUEST
        
        return Response(res,status=res_status)


    #define a Delete function in the API Class based views
    #keep in mind that while deleting an object we get PK directly on URL Not in the Request
    def delete(self, request, pk=None, format=None):
        student_data = StudentModel.objects.filter(pk=pk)
        if student_data.count()==0:
            res ={'status':0,'message':'No data found, Unable to Delete'}
            res_status = status.HTTP_400_BAD_REQUEST
        else:
            student_data.delete()
            res = {'status':1,'message':'Data found, Data delete Successfully','data':pk}
            res_status = status.HTTP_200_OK
        return Response(res, status=res_status)
