from rest_framework import viewsets
from .serializers import studentModelSerializer
from .models import studentModel
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .auth import myCustomAuthentication

"""
@ In this section we are going to implement the Token Authentication 
@ request.user will be a Django user instance
@ request.auth will be rest_framework.authtoken.models.Token instance
@ note: In production it must have https to make available the API
@ Token Generation  - using admin Application
                    - using Django manage.py drf_create_token <username>
                    - By Exposing an API endpoint
                    - using By Signals while Creating user

@ Also we have implemented the JSON Web Token for token Generation that are defined in the Urls.py file
    this requires to send the username and password with the request
"""
# lets create a class based api using rest_framework model View set and check the token authentication. That uses
# the myCustomAuthentication defined in the auth.py file. It requires to send username with the request
#  

class getStudentsWithTokenAuth_API(ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer
    authentication_classes = [myCustomAuthentication]
    permission_classes = [IsAuthenticated]