from rest_framework import viewsets
from .models import studentModel
from .serializers import studentModelSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import  AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly
#import Customer Permission From Customer Permission We have Created
from .customPermission import MyCustomPermission


"""
# Demostration of Model View set ReadOnly Model ViewSet
# demostration of SessionAuthentication and Persmission that we have provided with Rest Framewwork in Pemisions

"""

class studentModelViewSet_API(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    """
    @ BasicAuthentication- Login Required to have full access
    @ SessionAuthentication - Login Required but authenticates user by sessiond data
    """
    authentication_classes = [SessionAuthentication]
    
    """
    #Also we can Decalre Different Authentication and Permissions for different Function and Applications
    #here this permission class in going to Override Global IsAuthenticated permission Class
    #we have all ready declared Authentication In the Settings file Globally

    Note - Admim have full access by Default
    @ IsAuthenticatedReadOnly- Authenicated user full Access and Unauthenticated user Read Only Permission
    @ IsAdminUser- Only superUser or Staff or admin user full access
    @ AllowAny- Any one But Authenticated user will have full access
    @ DjangoModelPermissions - Authenticated Read only but after Django Model Permission can have full access 
        or Custom access we do it by django Admin Backend
    @ DjangoModelPermissionsOrAnonReadOnly - UnAuthenticated user Read Only but Authenticated user 
        and Django Model Perssions can have full access or Custom Depending upon the permissions granted
        we do it by django Admin Backend
    """
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [AllowAny]

#Lets Decalre another Function to have Limited access to the Student Resourses
#API will based on the Read only ViewSet
class studentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    #Basic Authentication will appied Globally
    #But Let Say we change Authentication Sytem, use Session Authentication instead
    #We will override the Basic Authentication System here
    #here IsAuthenticatd for all user types
    permission_classes = [IsAuthenticated]


"""
# Demostraion of Custom Permissions using Model ViewSet
"""
class studentModelViewCustomPermission_API(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer
    """
    
    """
    # authentication_classes = [SessionAuthentication]

    permission_classes = [MyCustomPermission]