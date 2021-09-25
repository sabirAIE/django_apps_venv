from .models import studentModel
from .serializers import studentModelSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .throttling import customRateThrottle

"""
@ Here we are going to implement the Thottling. Throttles indicate a temporary state, 
    and are used to control the rate of requests that clients can make to an API.
@ We have three main throttle classes in rest framework. 
    - userRateThrottle- used for registered user
        -This can also be customised as per need, We have to override the scope in order to do that
    - AnonRateThrottle- used for anonymous user
    - ScopedRateThrottle is used when we have different Api end point and we want to have different thrttling
        rate for each
    
    @ Note- We set Global scope and Throttle classes in the settings file, we have defined there go and see. 
"""

class getStudentThrottleLimit_API(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer
    authentication_classes = [SessionAuthentication]

    """
    @ Here for anonymous user read only rights are there and authenticated user have full access
        when we use the IsAuthenticatedOrReadOnly and for IsAuthenticated permission class we can only 
        authorize the registered users
    """
    # permission_classes=[IsAuthenticated]
    permission_classes= [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]


"""
@ Here we have implemented the custom Throttle rate using a user defined throttle class which inherits from 
    the builtin Class userRateThrottle and overrides the Scope properties
"""
class getStudentsThrottleAuthOnly_API(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [customRateThrottle]


"""
@ We are defining the Class based api view here to throttle a perticular opreration
    We have added this class based api to the URL but we will have to hit directly we are not going to
    get the this url in the route.

    Note: For scopedRateThottle we need class based api, function based api is not going to work with
        ScopedRateThrottle

@ Here we are going to override throttle_scope method with user defined Scope and this scope is going to set 
    in the Settings file under DEFAULT_THROTTLE_RATES
"""

class StudentDetailsClass(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'getData'

    #define a get function in the Class Based API View
    def get(self, request, pk=None, format= None):

        if pk is not None:
            student_data = studentModel.objects.filter(pk=pk)
            if student_data.count() == 0:
                res = {'status':0,'message':'No data Found or Invalid params Passed'}
                res_status = status.HTTP_400_BAD_REQUEST
            else:
                serial_data = studentModelSerializer(student_data,many=True)
                res = {'status':1,'message':'Data Found! Fetching data successfull','data':serial_data.data}
                res_status = status.HTTP_200_OK
            return Response(res, status=res_status)

        student_data = studentModel.objects.all()
        if student_data.count() == 0:
            res = {'status':0,'message':'No data Found'}
            res_status = status.HTTP_400_BAD_REQUEST
        else:
            serial_data = studentModelSerializer(student_data,many=True)
            res = {'status':1,'message':'Data Found! Fetching data successfull','data':serial_data.data}
            res_status = status.HTTP_200_OK
        return Response(res)
    
    #define a Post function in the API Class based View
    def post(self, request, format=None):
        post_data = request.data
        serial_data = studentModelSerializer(data=post_data)
        
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
        student_data = studentModel.objects.get(id=pk)
        serial_data = studentModelSerializer(student_data,data=request.data, partial=True)
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
        student_data = studentModel.objects.filter(pk=pk)
        if student_data.count()==0:
            res ={'status':0,'message':'No data found, Unable to Delete'}
            res_status = status.HTTP_400_BAD_REQUEST
        else:
            student_data.delete()
            res = {'status':1,'message':'Data found, Data delete Successfully','data':pk}
            res_status = status.HTTP_200_OK
        return Response(res, status=res_status)