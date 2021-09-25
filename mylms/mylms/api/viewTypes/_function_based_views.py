import io
from rest_framework.utils import json
from .serializers import StudentModelSerializer
from .models import StudentModel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#get a student by id
@api_view(['GET'])
def StudentDetail(request,pk=None):

    if pk is not None:
        student_data = StudentModel.objects.filter(pk=pk)

        if student_data.count() == 0:
            res = {'status':'error', 'message':'No Data Found or Invalid argument supplied'}
        else:
            serial_data = StudentModelSerializer(student_data, many=True)
            res = {'status': 'success', 'message':'Request successfully Processed','data':serial_data.data}
            
        return Response(res)
    #in case when pk is sent with the Request    
    student_data = StudentModel.objects.all()
    if student_data.count() == 0:
        raw = {'error':'Empty data','message':'No data available'}
    else:
        serial_data = StudentModelSerializer(student_data, many=True)
        res = {'status': 'success', 'message':'Request successfully Processed','data':serial_data.data}
    
    return Response(res)

#add a NEw Student
#@csrf_exempt this not required because we are handling the request from the APi View
@api_view(['POST','PUT','DELETE'])
def AddNewStudent(request):
    if request.method == 'POST':
        #Here We are using Api View that's why we are directly passing params to the serializer
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # py_data = JSONParser().parse(stream)

        serial_data = StudentModelSerializer(data = request.data)
        if serial_data.is_valid():
            serial_data.save()
            print(serial_data.validated_data)
            res = {'status':'success','message':'Student saved succesfully','data':serial_data.data}
        else:
            res = {'status':'error','message':serial_data.errors}
        
        return Response(res)
    
    #if Request is a PUT Request
    if request.method == 'PUT':
        #get Student first to instantite
        pk = request.data.get('id')

        #get  Student by the Given ID
        student  = StudentModel.objects.get(id=pk)
        serial_data = StudentModelSerializer(student, data=request.data, partial=True)

        #check for Valid Serial Data
        if serial_data.is_valid():
            serial_data.save()
            res = {'status':'success', 'message':'Data updated successfully','data':serial_data.data}
        else:
            res = {'status':'error', 'message':serial_data.errors}

        return Response(res)

    #if request id delete run delete operation
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        pk = py_data.get('id')

        #get student data first
        student_data = StudentModel.objects.filter(pk=pk)
        if student_data.count() == 0:
            res = {'status':'error','message':'No Data available to delete or Invalid argument Given'}
            json_res = json.dumps(res)
        else:
            student_data.delete()
            res = {'status':'success','message':'Data Deleted successfully'}
            json_res = json.dumps(res)

        return HttpResponse(json_res, content_type='application/json')
